class UserData(object):
    """Clase en la que se almacenan todos los parametros elegido por el usuario"""
    def __init__(self,f0=0, A=10, funcion="coseno", DC=50, f_sample=0):
        #Variables por default
        self.fo= f0
        self.Amp=A
        self.func= funcion
        self.DutyCycle= DC
        self.fs= f_sample

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



