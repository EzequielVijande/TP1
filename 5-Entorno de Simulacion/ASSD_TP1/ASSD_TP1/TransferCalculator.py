import UserData as u
import numpy as np
import math
import scipy.fftpack as fft
from scipy import signal
class TransferCalculator(object):
    """Clase que se encarga de calcular la salida de un bloque cualquiera conociendo la entrada"""
    def __init__(self):
        self.n=200
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
        (data.GetFAA()).clear()
        n=self.n
        fo= data.GetFo()
        wp =2.0*math.pi*(data.GetFc())
        ws= (1.5*wp)
        Ap= u.AP
        As= u.AS
        lp_filter = signal.iirdesign(wp=wp,ws=ws,gpass=Ap,gstop=As,analog=True,ftype='cheby2')
        t,data.FAA,x= signal.lsim(lp_filter,data.GetInput(),data.t)


        
        
    def CalculateSH_InTime(self,data):
        (data.GetSH()).clear()
        input= data.GetFAA()
        fs=data.GetFs()
        dc= data.GetDutyCycle()
        Thigh= (1/(fs*100.0))*dc
        sh_control = self.GenerateSquareWave(fs,Thigh,data.t)
        for i in range(0,len(data.t)):
            if(sh_control[i] == 1):
                data.SH.append(input[i])
            else:
                data.SH.append((data.SH)[i-1])


    def CalculateAnalogKeyInTime(self,data):
        return
    def CalculateOutputInTime(self,data):
        return
    #Funcion que pasa del dominio del tiempo a frecuencia
    def CalculateInFrecuency(self,data,x):
        fx= list(2*(fft.fft(x)/self.n) )

        (data.GetSignalInFrec()).clear()
        data.SignalInFrec = np.abs(fx)
        data.SignalInFrec = data.SignalInFrec[range(int(self.n/2))]
        data.f = np.linspace(0,1.0/(2.0*self.Ts),(self.n)/2)

    def GenerateSquareWave(self,fs,Thigh,t):
        T=1.0/fs
        square=[]
        for i in range(0,len(t)):
            if((t[i]%T) <= Thigh):
                square.append(1)
            else:
                square.append(0)
        return square


        

