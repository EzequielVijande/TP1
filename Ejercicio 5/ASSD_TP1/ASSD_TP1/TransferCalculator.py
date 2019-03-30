import UserData as u
import numpy as np
import math
import scipy.fftpack as fft
from scipy import signal
class TransferCalculator(object):
    """Clase que se encarga de calcular la salida de un bloque cualquiera conociendo la entrada"""
    def __init__(self):
        self.number_of_periods=6
        return
    #Funciones que calculan el valor de la funcion en un nodo
    def CalculateInputInTime(self,data):
        signal = data.GetFunc()
        A = data.GetAmp()
        fs = data.GetFs()
        if(data.GetFunc() != "AM"):
            fo = data.GetFo()
            T= 1.0/fo #Periodo de la funcion
            #defino incremento entre puntos del vector
            if(fs>=fo):
                self.Ts= 1.0/(100.0*fs)
            else:
                self.Ts= 1.0/(100.0*fo)
        else:
            T= 1.0/(data.AM_fm)
            fp_am = data.AM_fp
            #Defino incremento entre muestras para el caso de AM
            if(fs>= fp_am):
                self.Ts = 1.0/(100.0*fs)
            else:
                self.Ts= 1.0/(50.0*fp_am)

        t= np.array( np.arange(start=0,stop=(self.number_of_periods)*(T),step=self.Ts ))
        data.input= []
        data.t = t
        self.n = t.size #Numero de muestras
        if(signal == "coseno"):
            for i in range (0,t.size):
                data.input.append( A*(math.cos(2*(math.pi)*fo*(t[i]))) )
        elif(signal == "AM"):
            fp = data.AM_fp

            fm = data.AM_fm
            m = data.AM_m_index
            for i in range (0,t.size):
                aux= A*( (math.sin(2*(math.pi)*fp*(t[i])) ) + 0.5*m*( math.sin(2*(math.pi)*(fp+fm)*(t[i])) + math.sin(2*(math.pi)*(fp-fm)*(t[i]))) )
                data.input.append( aux )
        elif(signal == "x^2"):
            #coeficientes de fourier
            a0= (T**2)/12.0
            an=[]
            for i in range(1,41):
                aux= ((-1)**i)*( (T/(i*math.pi))**2)
                an.append(aux)
            for i in range (0,t.size):
                aux2=a0
                for j in range (0,len(an)):
                    aux2= aux2+ (an[j]*math.cos(2*(math.pi)*(j+1)*fo*(t[i])))
                aux2= A*aux2
                data.input.append(aux2)
        elif(signal == "(3/2)seno"):
            #coeficientes de fourier
            a0= 2.0/(3.0*math.pi)
            an=[]
            for i in range(1,41):
                first_term= math.cos( (0.5*math.pi)*( (2.0*i)- 3.0 ) )/( (2.0*i)-3.0 )
                second_term= (-1.0)* ( math.cos( (0.5*math.pi)*( (2.0*i)+ 3.0 ) )/( (2.0*i)+3.0 ) )
                third_term= 1.0/(  (2.0*i)+ 3.0 )
                fourth_term=  -1.0/(  (2.0*i) - 3.0 ) 
                aux= (2.0/(math.pi)) * ( (first_term) + (second_term) + (third_term) + (fourth_term))
                an.append(aux)
            for i in range (0,t.size):
                aux2=a0
                for j in range (0,len(an)):
                    aux2= aux2+ (an[j]*math.cos(2*(math.pi)*(j+1)*fo*(t[i])))
                aux2= aux2*A
                data.input.append(aux2)
    def CalculateFAA_InTime(self,data):
        fo= data.GetFo()
        wp =2.0*math.pi*(data.GetFc())
        ws= (1.5*wp)
        Ap= u.AP
        As= u.AS
        lp_filter = signal.iirdesign(wp=wp,ws=ws,gpass=Ap,gstop=As,analog=True,ftype=data.Aproximacion)
        t,data.FAA,x= signal.lsim(lp_filter,data.GetInput(),data.t)
        
        
    def CalculateSH_InTime(self,data):
        data.SH =[]
        input= data.GetFAA()
        fs=data.GetFs()
        Tsample= 1.0/fs
        dc= data.GetDutyCycle()
        Thigh= (dc/(fs*100.0))
        for i in range(0,len(input)):
            t_transcurrido = i*self.Ts
            number_of_period = math.floor(t_transcurrido/Tsample)
            remainder = t_transcurrido - (number_of_period*Tsample)
            if(remainder<= Thigh):
                data.SH.append(input[i]) #Esta en modo sample
            else:
                prev= data.SH[i-1]
                data.SH.append(prev) #Esta en modo Hold


    def CalculateAnalogKeyInTime(self,data):
        numero_de_periodo=0
        data.AnalogKey = []
        input = data.GetSH()
        fs= data.GetFs()
        Tsample= 1.0/fs
        dc= data.GetDutyCycle()
        Thigh= (1/(fs*100.0))*dc

        for i in range(0,len(input)):
            t_transcurrido = i*self.Ts
            number_of_period = math.floor(t_transcurrido/Tsample)
            remainder = t_transcurrido - (number_of_period*Tsample)
            if(remainder<= Thigh):
                data.AnalogKey.append(0) #Esta en modo sample
            else:
                data.AnalogKey.append(input[i]) #Esta en modo Hold

        

    def CalculateOutputInTime(self,data):
        input = data.GetAnalogKey()
        fo= data.GetFo()
        wp =2.0*math.pi*(data.GetFc())
        ws= (1.5*wp)
        Ap= u.AP
        As= u.AS
        lp_filter = signal.iirdesign(wp=wp,ws=ws,gpass=Ap,gstop=As,analog=True,ftype=data.Aproximacion)
        t,data.Output,x= signal.lsim(lp_filter,input,data.t)

    #Funcion que pasa del dominio del tiempo a frecuencia
    def CalculateInFrecuency(self,data,x):
        fx= list(2*(fft.fft(x)/self.n) )

        y = np.abs(fx)
        y = y[range(int(self.n/2))]
        data.f = np.linspace(0,1.0/(2.0*self.Ts),(self.n)/2)
        return y


        

