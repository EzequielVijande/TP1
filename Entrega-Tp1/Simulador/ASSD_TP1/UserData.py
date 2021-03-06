import numpy as np
#Constantes de la plantilla del filtro
AP=1
AS=41

class UserData(object):
    """Clase en la que se almacenan todos los parametros elegido por el usuario"""
    def __init__(self,f0=0, A=10, funcion="coseno", DC=50, f_sample=0, fc=0):
        #Variables por default
        self.fo= f0
        self.Amp=A
        self.func= funcion
        self.DutyCycle= DC
        self.fs= f_sample
        self.fc =fc
        self.Aproximacion=""
        #Parametros para funcion AM
        self.AM_fp=0
        self.AM_fm=0
        self.AM_m_index=1
        #Resultados
        self.input=[]
        self.FAA=[]
        self.AnalogKey=[]
        self.SH=[]
        self.Output=[]
        self.t=[] #vector con la abscisa del tiempo
        self.f=[] #vector con la abscisa de las frecuencias
        #Vectores en frecuencia
        self.InputInFrec=[]
        self.FAA_InFrec=[]
        self.SH_InFrec=[]
        self.AnalogKeyInFrec=[]
        self.OutputInFrec=[]

    #Getters
    def GetFo(self):
        return (self.fo)

    def GetAmp(self):
        return (self.Amp)

    def GetFunc(self):
        return (self.func)

    def GetDutyCycle(self):
        return (self.DutyCycle)

    def GetFs(self):
        return (self.fs)

    def GetFc(self):
        return (self.fc)

    def GetInput(self):
        return self.input

    def GetFAA(self):
        return self.FAA

    def GetSH(self):
        return self.SH

    def GetAnalogKey(self):
        return self.AnalogKey

    def GetOutput(self):
        return self.Output

    def GetTimeVector(self):
        return (self.t)

    def GetFrequencyVector(self):
        return (self.f)
    

