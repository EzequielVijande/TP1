import GUI as g
import UserData as u
import TransferCalculator as t

#Estados
TIEMPO=0
FRECUENCIA=1
EXIT=2
class Manager(object):
    """Clase que se encarga de manejar los eventos generados"""
    def __init__(self,GUI,data,calculator):
        self.GUI=GUI
        self.Data= data
        self.calc= calculator
        self.estado= TIEMPO
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
        selected = self.GUI.GetSelectedDomain()
        if( (selected == g.TIME)and(self.estado != TIEMPO)):
            self.estado = TIEMPO
            self.OnPlotEv()
        elif((selected == g.FREQ)and(self.estado != FRECUENCIA)):
            self.estado= FRECUENCIA
            self.OnPlotEv()

    def OnPlotEv(self):
        graph_to_plot= self.GUI.GetSelectedPlot()
        #Validar input
        #Actualizar los parametros de input
        self.UpdateUserData()
        self.CalculateAllNodes()
        self.CalculateHarmonics()
   
        self.ShowGraph()
    
                     
    def Error(self):
        return

    def UpdateUserData(self):
        self.Data.Amp =  float(self.GUI.InpAmpString.get() )
        self.Data.func = (self.GUI.selected_func.get())

        if( self.Data.func == "AM"):
            self.Data.AM_fp = float(self.GUI.InpAmFpString.get())
            self.Data.AM_fm = float(self.GUI.InpAmFmString.get())
            self.Data.AM_m_index = self.GUI.SlideAmIndex.get()
        else:
             self.Data.fo = float(self.GUI.InpFrecString.get())

        self.Data.fs = float(self.GUI.SamplerFsString.get())
        self.Data.fc = float(self.GUI.FilterFcString.get())
        self.Data.DutyCycle= self.GUI.SlideDC.get()
        self.Data.Aproximacion= self.GUI.SelectedAprox.get()


    def CalculateAllNodes(self):
        self.calc.CalculateInputInTime(self.Data)
        if(self.GUI.BypassFAA.get() == g.BYPASS_OFF):
            self.calc.CalculateFAA_InTime(self.Data)
        else:
            self.Data.FAA = self.Data.input
        if(self.GUI.BypassSH.get() == g.BYPASS_OFF):
            self.calc.CalculateSH_InTime(self.Data)
        else:
            self.Data.SH = self.Data.FAA
        if(self.GUI.BypassKey.get() == g.BYPASS_OFF):
            self.calc.CalculateAnalogKeyInTime(self.Data)
        else:
            self.Data.AnalogKey = self.Data.GetSH()
        if(self.GUI.BypassFR.get() == g.BYPASS_OFF):
            self.calc.CalculateOutputInTime(self.Data)
        else:
            self.Data.Output = self.Data.AnalogKey

    def CalculateHarmonics(self):
        self.Data.InputInFrec= self.calc.CalculateInFrecuency(self.Data,self.Data.GetInput())
        self.Data.FAA_InFrec= self.calc.CalculateInFrecuency(self.Data,self.Data.GetFAA())
        self.Data.SH_InFrec= self.calc.CalculateInFrecuency(self.Data,self.Data.GetSH())
        self.Data.AnalogKeyInFrec= self.calc.CalculateInFrecuency(self.Data,self.Data.GetAnalogKey())
        self.Data.OutputInFrec= self.calc.CalculateInFrecuency(self.Data,self.Data.GetOutput())

    def ShowGraph(self):
        Xmin=0
        Xmax=0
        Ymin=0
        Ymax=0
        f= self.Data.GetFrequencyVector()
        #Harmonicos
        y_inp =self.Data.InputInFrec
        y_faa = self.Data.FAA_InFrec
        y_sh = self.Data.SH_InFrec
        y_key = self.Data.AnalogKeyInFrec
        y_out = self.Data.OutputInFrec

        self.GUI.Axes.cla()
        self.GUI.PlotInput(self.Data.t,self.Data.GetInput())
        self.GUI.PlotA(self.Data.t,self.Data.GetFAA())
        self.GUI.PlotB(self.Data.t,self.Data.GetSH())
        self.GUI.PlotC(self.Data.t,self.Data.GetAnalogKey())
        self.GUI.PlotOutput(self.Data.t,self.Data.GetOutput())

        Xmin,Xmax,Ymin,Ymax= self.ObtainScaleLimits()
        self.GUI.DisplaySelectedGraph(Xmin,Xmax,Ymin,Ymax,f,y_inp,y_faa,y_sh,y_key,y_out)

    def ObtainScaleLimits(self):
        selected_graph = (self.GUI.GetSelectedPlot())
        Xmin=0
        Xmax=max(self.Data.GetTimeVector())
        Ymin=0
        Ymax=0
        if(self.estado==TIEMPO):
            if(selected_graph == g.INPUT):
                Ymin= min(self.Data.GetInput())
                Ymax= max(self.Data.GetInput())
            elif(selected_graph == g.A):
                Ymin= min(self.Data.GetFAA())
                Ymax= max(self.Data.GetFAA())
            elif(selected_graph == g.B):
                Ymin= min(self.Data.GetSH())
                Ymax= max(self.Data.GetSH())
            elif(selected_graph == g.C):
                Ymin= min(self.Data.GetAnalogKey())
                Ymax= max(self.Data.GetAnalogKey())
            elif(selected_graph == g.OUTPUT):
                Ymin= min(self.Data.GetOutput())
                Ymax= max(self.Data.GetOutput())
        elif(self.estado == FRECUENCIA):
            Xmax= 15*(self.Data.fo)
            Ymin=0
            if(selected_graph == g.INPUT):
                Ymax= 1.2*max(self.Data.InputInFrec)
            elif(selected_graph == g.A):
                Ymax= 1.2*max(self.Data.FAA_InFrec)
            elif(selected_graph == g.B):
                Ymax= 1.2*max(self.Data.SH_InFrec)
            elif(selected_graph == g.C):
                Ymax= 1.2*max(self.Data.AnalogKeyInFrec)
            elif(selected_graph == g.OUTPUT):
                Ymax= 1.2*max(self.Data.OutputInFrec)
        return Xmin, Xmax, Ymin, Ymax


