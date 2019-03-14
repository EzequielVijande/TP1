import GUI as g

#Estados
INICIAL=0
EXIT=1
class Manager(object):
    """Clase que se encarga de manejar los eventos generados"""
    def __init__(self,GUI):
        self.GUI=GUI
        self.estado= INICIAL
    def Dispatch(self, ev):
            if(ev == g.NO_EV):
                self.OnNoEv()
            elif(ev == g.QUIT_EV):
                self.OnQuitEv()
            else:
                self.Error()

            self.GUI.EventSolved()    #Settea que ya no hay evento a resolver

    #Getters
    def getState(self):
        return self.estado


    #Funciones que manejan eventos

    def OnNoEv(self):
        return

    def OnFAAEv(self):
        return

    def OnQuitEv(self):
        self.GUI.CloseGUI()
        self.estado=EXIT
        return

    def Error(self):
        return


