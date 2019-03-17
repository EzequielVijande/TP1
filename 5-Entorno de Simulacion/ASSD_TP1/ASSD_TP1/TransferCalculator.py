import UserData as u
import numpy as np
import math
import scipy.fftpack as fft
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
            t= np.array( np.arange(start=0,stop=(4*T),step=self.Ts ))
            data.input.clear()
            for i in range (0,t.size):
                data.input.append( A*(math.cos(2*(math.pi)*fo*(t[i]))) )
            data.t = t
    def CalculateFAA_InTime(self,data):
        n=self.n
        fo= data.GetFo()
        fc =data.GetFc()
        t= np.array( np.arange(start=0,stop=(4/fc),step=self.Ts ))
        funcLP = ( math.sin(2*math.pi*fc*t))/(2*math.pi*fc*t)
        previous_node= list((fft.fft(data.GetInput())) )
        (data.GetFAA()).clear()
        data.FAA = np.real(fft.ifft(previous_node))
        
        
    def CalculateSH_InTime(self,data):
        return
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



