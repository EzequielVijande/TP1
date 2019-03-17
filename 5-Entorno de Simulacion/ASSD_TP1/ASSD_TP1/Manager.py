import GUI as g
import UserData as u

#Estados
INICIAL=0
EXIT=1
class Manager(object):
    """Clase que se encarga de manejar los eventos generados"""
    def __init__(self,GUI,data):
        self.GUI=GUI
        self.Data= data
        self.estado= INICIAL
    def Dispatch(self, ev):
            if(ev == g.NO_EV):
                self.OnNoEv()
            elif(ev == g.QUIT_EV):
                self.OnQuitEv()
            elif(ev == g.TIME_FREQ_BUTTON_EV):
                self.OnTimeFreqEv()
            elif(ev == g.PLOT_BUTTON_EV):
                self.OnPlotEv()
            else:
                self.Error()

            self.GUI.EventSolved()    #Settea que ya no hay evento a resolver


    #Getters
    def getState(self):
        return self.estado


    #Funciones que manejan eventos

    def OnNoEv(self):
        return

    def OnQuitEv(self):
        self.GUI.CloseGUI()
        self.estado=EXIT
        return

    def OnTimeFreqEv(self):
        return

    def OnPlotEv(self):
        graph_to_plot= self.GUI.GetSelectedPlot()
        #Validar input
        #Actualizar los parametros de input
        self.UpdateUserData()
      #  if(graph_to_plot == g.INPUT):

        #elif(graph_to_plot == g.A):

    def Error(self):
        return

    def UpdateUserData(self):
        self.Data.Amp =  float(self.GUI.InpAmpString.get() )
        self.Data.fo = float(self.GUI.InpFrecString.get())
        self.Data.func = (self.GUI.selected_func.get())
        self.Data.fs = float(self.GUI.SamplerFsString.get())


