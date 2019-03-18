import UserData as u
import numpy as np
import math
import scipy.fftpack as fft
from scipy import signal
class TransferCalculator(object):
    """Clase que se encarga de calcular la salida de un bloque cualquiera conociendo la entrada"""
    def __init__(self):
        self.n=500
        return
    #Funciones que calculan el valor de la funcion en un nodo
    def CalculateInputInTime(self,data):
        signal = data.GetFunc()
        fo = data.GetFo()
        A = data.GetAmp()
        T= 1/fo #Periodo de la funcion
        self.Ts= (4*T)/(self.n)
        if(signal == "coseno"):
            t= np.array( np.arange(start=0,stop=(self.n)*(self.Ts),step=self.Ts ))
            data.input.clear()
            for i in range (0,t.size):
                data.input.append( A*(math.cos(2*(math.pi)*fo*(t[i]))) )
            data.t = t
    def CalculateFAA_InTime(self,data):
        n=self.n
        fo= data.GetFo()
        wp =2.0*math.pi*(data.GetFc())
        ws= (1.5*wp)
        Ap= u.AP
        As= u.AS
        lp_filter = signal.iirdesign(wp=wp,ws=ws,gpass=Ap,gstop=As,analog=True,ftype='cheby2')
        t,data.FAA,x= signal.lsim(lp_filter,data.GetInput(),data.t)


        
        
    def CalculateSH_InTime(self,data):
        numero_de_periodo=0
        start=0 #indice en el que empieza a muestrearse un nuevo periodo
        (data.GetSH()).clear()
        input= data.GetFAA()
        fs=data.GetFs()
        dc= data.GetDutyCycle()
        Thigh= (dc/(fs*100.0))
        t_control,sh_control = self.GenerateSquareWave(fs,Thigh,data.t)
        samples_per_period= int(1000/dc)
        for i in range(0,len(data.t)):
            k=int(i*(self.Ts)*(10.0/Thigh)) #Mappeo el indice de data.t al que mejor corresponde para la cuadrada
            if(k==len(sh_control)):
                k=k-1
            if(sh_control[k] == 1):
                data.SH.append(input[i])
            else:
                numero_de_periodo=np.floor(k/samples_per_period)
                start=int(numero_de_periodo*samples_per_period)+10
                l=int(start*(Thigh/(10*self.Ts)))
                if(l>= len(input)):
                    l= len(input)-1
                data.SH.append(input[l])


    def CalculateAnalogKeyInTime(self,data):
        numero_de_periodo=0
        start=0 #indice en el que empieza a muestrearse un nuevo periodo
        (data.GetAnalogKey()).clear()
        input = data.GetSH()
        fs= data.GetFs()
        dc= data.GetDutyCycle()
        Thigh= (1/(fs*100.0))*dc
        t_sq,key_control = self.GenerateSquareWave(fs,Thigh,data.t)
        samples_per_period= int(1000/dc)
        for i in range(0,len(data.t)):
            k=int(np.floor(i*(self.Ts)*(10.0/Thigh))) #Mappeo el indice de data.t al que mejor corresponde para la cuadrada
            if(k == len(key_control)):
               k=k-1
            if(key_control[k] == 1):
                data.AnalogKey.append(0)
            else:
                numero_de_periodo=np.floor(k/samples_per_period)
                start=int(numero_de_periodo*samples_per_period)+10
                l=int(start*(Thigh/(10*self.Ts)))
                if(l>= len(input)):
                    l=len(input)-1
                data.AnalogKey.append(input[l])

    def CalculateOutputInTime(self,data):
        input = data.GetAnalogKey()
        fo= data.GetFo()
        wp =2.0*math.pi*(data.GetFc())
        ws= (1.5*wp)
        Ap= u.AP
        As= u.AS
        lp_filter = signal.iirdesign(wp=wp,ws=ws,gpass=Ap,gstop=As,analog=True,ftype='cheby2')
        t,data.Output,x= signal.lsim(lp_filter,input,data.t)

    #Funcion que pasa del dominio del tiempo a frecuencia
    def CalculateInFrecuency(self,data,x):
        fx= list(2*(fft.fft(x)/self.n) )

        y = np.abs(fx)
        y = y[range(int(self.n/2))]
        data.f = np.linspace(0,1.0/(2.0*self.Ts),(self.n)/2)
        return y

    def GenerateSquareWave(self,fs,Thigh,t):
        T=1.0/fs
        t_square= np.arange(start=0,stop=t[-1],step=Thigh/10)
        square=[]
        for i in range(0,len(t_square)):
            if((t_square[i]%T) <= Thigh):
                square.append(1)
            else:
                square.append(0)
        return t_square,square


        

