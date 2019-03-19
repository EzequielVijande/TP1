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
            elif(ev == g.INPUT_CHANGED_EV):
                self.OnInputChangedEv()
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

    def OnInputChangedEv(self):
        if(self.GUI.graphed_once):
            self.OnPlotEv()

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
        result_str= self.ValidateInput()
        if(result_str!="Ok"):
            self.GUI.ShowMessage(result_str)
        else:
            self.GUI.graphed_once = True
            if(self.GUI.input_changed):
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
        func = self.Data.GetFunc()
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
            if(func != "AM"):
                Xmax= 15*(self.Data.fo)
            else:
                Xmax= 2*self.Data.AM_fp
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

    def isfloat(self,value):
      try:
        float(value)
        return True
      except ValueError:
        return False

    def IsValidNumber(self,arg, argstring):
        if( self.isfloat(arg)): #valido el argumento
            arg_f=float(arg)
            if(arg_f<=0):
                return ( argstring+" debe ser positivo")
            elif(arg_f==float("inf")):
                return (argstring+" debe tener un valor finito")

        else:
            return ("Error de sintaxis en "+argstring)

        return "Ok" #El numero parece ser valido

    def ValidateInput(self):
        func = self.GUI.GetSelectedFunc()
        type_of_plot = self.GUI.GetSelectedPlot()
        #Valido la amplitud
        A_str = self.IsValidNumber(self.GUI.InpAmpString.get(),"A")
        if(A_str != "Ok"):
            return A_str
        if(func == "AM"):
            fpStr = self.IsValidNumber(self.GUI.InpAmFpString.get(),"fp")
            if(fpStr != "Ok"):
                return fpStr
            fmStr = self.IsValidNumber(self.GUI.InpAmFmString.get(),"fm")
            if(fmStr != "Ok"):
                return fmStr
            fp = float(self.GUI.InpAmFpString.get())
            fm = float(self.GUI.InpAmFmString.get())
            if(fm >= fp):
                return "fm debe ser menor que fp"
        else:
            foStr = self.IsValidNumber(self.GUI.InpFrecString.get(),"fo")
            if(foStr != "Ok"):
                return foStr


        fcStr = self.IsValidNumber(self.GUI.FilterFcString.get(),"fc")
        if( fcStr != "Ok"):
            return fcStr
        fsStr = self.IsValidNumber(self.GUI.SamplerFsString.get(), "fs")
        if( fsStr != "Ok"):
            return fsStr

        return "Ok"




