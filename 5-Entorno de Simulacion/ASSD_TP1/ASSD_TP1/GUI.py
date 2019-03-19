import matplotlib
import matplotlib.patches as patches
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
from pathlib import Path
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

#Eventos
NO_EV=0
QUIT_EV=1
TIME_FREQ_BUTTON_EV=2
PLOT_BUTTON_EV=3
INPUT_CHANGED_EV=4


#Largos y Anchos
GRAPH_WIDTH=600
GRAPH_HEIGHT=450

#Colores
FRAME_COLOR= "goldenrod"
FRAME_TEXT_COLOR="black"
BUTTON_COLOR= "light goldenrod"
BUTTON_FONT_COLOR="black"
GRAPH_BUTTON_COLOR="Cyan1"
GRAPH_BUTTON_TEXT_COLOR="black"

#Funciones
FUNCIONES=[
    "coseno",
    "AM",
    "x^2",
    "(3/2)seno"
    ]
#Aproximaciones
APROXIMACIONES=[
    "butter",
    "cheby1",
    "cheby2",
    "ellip"]
#Nodos
A=1
B=2
C=3
INPUT=4
OUTPUT=5
#Graficas
TIME=1
FREQ=2
#Bypass
BYPASS_ON=1
BYPASS_OFF=2

class SimGUI:
    """Clase que se encarga de manejar la interfaz grafic de la simulacion"""
    def __init__(self):
        self.graphed_once= False
        self.input_changed= False
        self.ShowingAmParameters = False #flag que indica que se muestran las entradas para unna funcion AM
        #Flags para graficas discretas
        self.Inp_is_in_plot= False
        self.FAA_is_in_plot=False
        self.SH_is_in_plot=False
        self.AnalogKey_is_in_plot=False
        self.Output_is_in_plot=False

        self.Ev=NO_EV
        self.root = Tk()
        self.root.geometry('1620x780')
        self.root.resizable(width=True, height=True)
        self.root.title("Simulador de muestreo")
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.CreateScheme()
        self.CreatePlot()
        self.CreateOptions()

    def CreateScheme(self):
        #Region donde esta el dibujo del circuito
        self.SchemeFrame = LabelFrame(master=self.root, text="Esquema del circuito",background=FRAME_COLOR,fg=FRAME_TEXT_COLOR)
        self.SchemeFrame.grid(row=0,column=0,sticky=N+S+W+E)
        self.photo = PhotoImage(file=".\Imagenes\esquema.PGM")
        self.SchemeLabel = Label(master=self.SchemeFrame,image= self.photo)
        self.SchemeLabel.grid(row=0,sticky=N+S+W+E,ipady=100)
        self.PlaceButtons()

    def CreatePlot(self):
        #Region donde se grafican las funciones
        self.PlotFrame = LabelFrame(master=self.root, text="Grafica",background=FRAME_COLOR,fg=FRAME_TEXT_COLOR)
        self.PlotFrame.grid(row=0,column=1,sticky=N+S+W+E)
        self.fig=Figure(figsize=(1,1), dpi=200,facecolor="lavender",constrained_layout=True)
        self.Graph = FigureCanvasTkAgg(self.fig,master=self.PlotFrame)
        self.Graph.get_tk_widget().config( width=GRAPH_WIDTH, height=GRAPH_HEIGHT)
        self.Graph.get_tk_widget().grid(row=0)
        #Creo una toolbar para los graficos
        self.toolbarFrame = Frame(master=self.PlotFrame)
        self.toolbarFrame.grid(row=1)
        toolbar = NavigationToolbar2Tk(self.Graph, self.toolbarFrame)
        toolbar.grid(row=0)
        #Inicializo Axes
        self.InitializeAxes()

        #Botones para cambiar de graficas
        self.SelectedGraph= tk.IntVar()
        self.GraphButtonFrame = Frame(master=self.PlotFrame)
        self.GraphButtonFrame.grid(row=2)
        self.TimeButton= Radiobutton(master=self.GraphButtonFrame,text="En tiempo",background=GRAPH_BUTTON_COLOR,fg=GRAPH_BUTTON_TEXT_COLOR,
                                     indicatoron=False,variable=self.SelectedGraph,value=TIME,command=self.change_domain_of_graph_call)
        self.TimeButton.grid(row=0,column=0,sticky=W+E)
        self.FreqButton= Radiobutton(master=self.GraphButtonFrame,text="En frecuencia",background=GRAPH_BUTTON_COLOR,fg=GRAPH_BUTTON_TEXT_COLOR,
                                     indicatoron=False,variable=self.SelectedGraph,value=FREQ,command=self.change_domain_of_graph_call)
        self.FreqButton.grid(row=0,column=1,sticky=W+E)
        self.TimeButton.select() #empieza en tiempo por default
    def CreateOptions(self):
        #Region con los parametros posibles
        self.OptionsFrame = LabelFrame(master=self.root, text="Parametros",background=FRAME_COLOR,fg=FRAME_TEXT_COLOR)
        self.OptionsFrame.grid(row=100,sticky=W+E+S+N,columnspan=10,ipady=20)
        self.CreateInputSection()
        self.CreateFilterSection()
        self.CreateSamplerSection()

    def CreateInputSection(self):
        self.InpAmpString= StringVar()
        self.InpFrecString= StringVar()
        self.InpAmFpString= StringVar()
        self.InpAmFmString= StringVar()

        self.InputFrame = LabelFrame(master=self.OptionsFrame, text="Entrada",background=FRAME_COLOR,fg=FRAME_TEXT_COLOR)
        self.InputFrame.grid(row=0,column=0,sticky=S+N)
        self.selected_func = StringVar(master=self.InputFrame)
        self.selected_func.set(FUNCIONES[0]) # Empieza con coseno como default
        self.pull_down_menu = OptionMenu(self.InputFrame, self.selected_func, *FUNCIONES)
        self.pull_down_menu.config(bg=BUTTON_COLOR)
        self.pull_down_menu.grid(row=0,sticky=W+E)
        #Creo las entradas de frecuencia y amplitud
        self.InpFrecLabel= Label(master=self.InputFrame,text="fo(Hz)",anchor=W,background=BUTTON_COLOR,fg=BUTTON_FONT_COLOR)
        self.InpFrecLabel.grid(row=1,column=0,sticky=W+E)
        self.entry_inp_fo=Entry(master=self.InputFrame,textvariable=self.InpFrecString)
        self.entry_inp_fo.grid(row=1,column=1,ipadx=120)

        #Entradas para funcion AM
        self.InpFpLabel = Label(master=self.InputFrame,text="fp(Hz)",anchor=W,background=BUTTON_COLOR,fg=BUTTON_FONT_COLOR)
        self.entry_inp_fp=Entry(master=self.InputFrame,textvariable=self.InpAmFpString)

        self.InpFmLabel= Label(master=self.InputFrame,text="fm(Hz)",anchor=W,background=BUTTON_COLOR,fg=BUTTON_FONT_COLOR)
        self.entry_inp_fm=Entry(master=self.InputFrame,textvariable=self.InpAmFmString)

        self.AmIndexLabel= Label(master=self.InputFrame,text="m",anchor=W,background=BUTTON_COLOR,fg=BUTTON_FONT_COLOR)
        self.SlideAmIndex= Scale(master=self.InputFrame, from_=0.01, to=1,resolution=0.01,orient=HORIZONTAL,command= self.input_change_callback)
        self.SlideAmIndex.config(bg=BUTTON_COLOR)

        self.InpAmpLabel= Label(master=self.InputFrame,text="Amp(V)",anchor=W,background=BUTTON_COLOR,fg=BUTTON_FONT_COLOR)
        self.InpAmpLabel.grid(row=2,column=0,sticky=W+E)
        self.entry_inp_amp= Entry(master=self.InputFrame,textvariable=self.InpAmpString)
        self.entry_inp_amp.grid(row=2,column=1,sticky=W+E)
        #Trackeo de la funcion de input
        self.selected_func.trace("w",self.selected_func_callback)
        self.InpAmpString.trace("w",self.input_change_callback)
        self.InpFrecString.trace("w",self.input_change_callback)
        self.InpAmFpString.trace("w",self.input_change_callback)
        self.InpAmFmString.trace("w",self.input_change_callback)

    def CreateFilterSection(self):
        self.FilterFcString= StringVar()
        self.SelectedAprox = StringVar()
        self.SelectedAprox.set("cheby2")
        self.BypassFAA = IntVar()
        self.BypassFR = IntVar()

        self.FilterFrame = LabelFrame(master=self.OptionsFrame, text="Filtros",background=FRAME_COLOR,fg=FRAME_TEXT_COLOR)
        self.FilterFrame.grid(row=0,column=1,sticky=S+N)
        #Frecuencia de corte de los filtros
        self.FilterFcLabel= Label(master=self.FilterFrame,text="fc(Hz)",anchor=W,background=BUTTON_COLOR,fg=BUTTON_FONT_COLOR)
        self.FilterFcLabel.grid(row=0,column=0,sticky=W+E)
        self.entry_filter_fc= Entry(master=self.FilterFrame,textvariable=self.FilterFcString)
        self.entry_filter_fc.grid(row=0,column=1,sticky=W+E,ipadx=120)
        #Botones de Bypass
        self.FAA_BypassButton= Checkbutton(master=self.FilterFrame, text="Bypass FAA",command= self.input_change_callback,
                        variable=self.BypassFAA,onvalue=BYPASS_ON, offvalue=BYPASS_OFF,background=BUTTON_COLOR,fg=BUTTON_FONT_COLOR)
        self.FAA_BypassButton.grid(row=1,column=0,sticky=W+E)
        self.FR_BypassButton= Checkbutton(master=self.FilterFrame, text="Bypass FR",command= self.input_change_callback,
                        variable=self.BypassFR,onvalue=BYPASS_ON, offvalue=BYPASS_OFF,background=BUTTON_COLOR,fg=BUTTON_FONT_COLOR)
        self.FR_BypassButton.grid(row=1,column=1,sticky=W+E)

        #Aproximacion
        self.approx_menu = OptionMenu(self.FilterFrame, self.SelectedAprox, *APROXIMACIONES)
        self.approx_menu.config(bg=BUTTON_COLOR)
        self.approx_menu.grid(row=2,sticky=W+E)

        #Desselecciono los botones
        self.FAA_BypassButton.deselect()
        self.FR_BypassButton.deselect()
        #Trackeo de las variables
        self.FilterFcString.trace("w",self.input_change_callback)
        self.SelectedAprox.trace("w",self.input_change_callback)

    def CreateSamplerSection(self):
        #Variables
        self.SamplerFsString= StringVar()
        self.BypassSH= IntVar()
        self.BypassKey= IntVar()
        self.SamplerFrame = LabelFrame(master=self.OptionsFrame, text="Muestreo",background=FRAME_COLOR,fg=FRAME_TEXT_COLOR)
        self.SamplerFrame.grid(row=0,column=2,sticky=S+N)
        #Entrada para la frecuencia de sampleo
        self.SamplerFsLabel= Label(master=self.SamplerFrame,text="fs(Hz)",anchor=W,background=BUTTON_COLOR,fg=BUTTON_FONT_COLOR)
        self.SamplerFsLabel.grid(row=0,column=0,sticky=N+S+W+E)
        self.entry_sampler_fs= Entry(master=self.SamplerFrame,textvariable=self.SamplerFsString)
        self.entry_sampler_fs.grid(row=0,column=1,sticky=W+E,ipadx=70)
        #Duty cycle
        self.SlideDC_Label = Label(master=self.SamplerFrame,text="DC(%)",anchor=W,background=BUTTON_COLOR,fg=BUTTON_FONT_COLOR)
        self.SlideDC_Label.grid(row=1,column=0,sticky=N+S+W+E)
        self.SlideDC = Scale(master=self.SamplerFrame, from_=0, to=100,orient=HORIZONTAL,command= self.input_change_callback)
        self.SlideDC.config(bg=BUTTON_COLOR)
        self.SlideDC.grid(row=1,column=1,sticky=W+E,ipadx=120)
        #Botones de Bypass
        self.SH_BypassButton= Checkbutton(master=self.SamplerFrame, text="Bypass SH",command= self.input_change_callback,
                        variable=self.BypassSH,onvalue=BYPASS_ON, offvalue=BYPASS_OFF,background=BUTTON_COLOR,fg=BUTTON_FONT_COLOR)
        self.SH_BypassButton.grid(row=2,column=0,sticky=W+E)
        self.KEY_BypassButton= Checkbutton(master=self.SamplerFrame, text="Bypass Key",command= self.input_change_callback,
                        variable=self.BypassKey,onvalue=BYPASS_ON, offvalue=BYPASS_OFF,background=BUTTON_COLOR,fg=BUTTON_FONT_COLOR)
        self.KEY_BypassButton.grid(row=2,column=1,sticky=W+E)

        self.SH_BypassButton.deselect()
        self.KEY_BypassButton.deselect()
        #Trackeo de variables
        self.SamplerFsString.trace("w", self.input_change_callback)

    def PlaceButtons(self):
        self.SelectedPlot = IntVar()
        self.SchemeButtonFrame= Frame(master=self.SchemeFrame)
        self.SchemeButtonFrame.grid(row=1,sticky=N+S+W+E)
        #Botones
        self.PlotInput_Button= Radiobutton(master=self.SchemeButtonFrame,text="Plot Xin",background=GRAPH_BUTTON_COLOR,fg=GRAPH_BUTTON_TEXT_COLOR,
                                     indicatoron=False,variable=self.SelectedPlot,value=INPUT,command=self.change_graph_button_call)
        self.PlotInput_Button.grid(row=0,column=0,sticky=N+S+W+E,ipadx=40)
        self.PlotNodeA_Button= Radiobutton(master=self.SchemeButtonFrame,text="Plot Node A",background=GRAPH_BUTTON_COLOR,fg=GRAPH_BUTTON_TEXT_COLOR,
                                     indicatoron=False,variable=self.SelectedPlot,value=A,command=self.change_graph_button_call)
        self.PlotNodeA_Button.grid(row=0,column=1,sticky=N+S+W+E,ipadx=40)
        self.PlotNodeB_Button= Radiobutton(master=self.SchemeButtonFrame,text="Plot Node B",background=GRAPH_BUTTON_COLOR,fg=GRAPH_BUTTON_TEXT_COLOR,
                                     indicatoron=False,variable=self.SelectedPlot,value=B,command=self.change_graph_button_call)
        self.PlotNodeB_Button.grid(row=0,column=2,sticky=N+S+W+E,ipadx=40)
        self.PlotNodeC_Button= Radiobutton(master=self.SchemeButtonFrame,text="Plot Node C",background=GRAPH_BUTTON_COLOR,fg=GRAPH_BUTTON_TEXT_COLOR,
                                     indicatoron=False,variable=self.SelectedPlot,value=C,command=self.change_graph_button_call)
        self.PlotNodeC_Button.grid(row=0,column=3,sticky=N+S+W+E,ipadx=40)
        self.PlotOutput_Button= Radiobutton(master=self.SchemeButtonFrame,text="Plot Xout",background=GRAPH_BUTTON_COLOR,fg=GRAPH_BUTTON_TEXT_COLOR,
                                     indicatoron=False,variable=self.SelectedPlot,value=OUTPUT,command=self.change_graph_button_call)
        self.PlotOutput_Button.grid(row=0,column=4,sticky=N+S+W+E,ipadx=50)

    #Getters
    def GetEvent(self):
        return self.Ev
    def GetSelectedPlot(self):
        return ( self.SelectedPlot.get() )
    def GetSelectedDomain(self):
        return (self.SelectedGraph.get())
    def GetSelectedFunc(self):
        return self.selected_func.get()

    #Funciones de la grafica
    def InitializeAxes(self):
        self.Axes= self.fig.add_subplot(111)
        self.Axes.set_axis_off()

    def HideAllLines(self):
        self.Input_lines.set_visible(False)
        self.NodeA_lines.set_visible(False)
        self.NodeB_lines.set_visible(False)
        self.NodeC_lines.set_visible(False)
        self.Output_lines.set_visible(False)
        if(self.Inp_is_in_plot):
            self.Inp_container.remove()
            self.Inp_is_in_plot=False
        elif(self.FAA_is_in_plot):
            self.FAA_container.remove()
            self.FAA_is_in_plot= False
        elif(self.SH_is_in_plot):
            self.SH_container.remove()
            self.SH_is_in_plot= False
        elif(self.AnalogKey_is_in_plot):
            self.AnalogKey_container.remove()
            self.AnalogKey_is_in_plot= False
        elif(self.Output_is_in_plot):
            self.Output_container.remove()
            self.Output_is_in_plot= False

    def PlotInput(self,t,y):
        self.Input_lines, =self.Axes.plot(t,y)

    def PlotA(self,t,y):
        self.NodeA_lines, =self.Axes.plot(t,y)

    def PlotB(self,t,y):
        self.NodeB_lines, =self.Axes.plot(t,y)

    def PlotC(self,t,y):
        self.NodeC_lines, =self.Axes.plot(t,y)

    def PlotOutput(self,t,y):
        self.Output_lines, =self.Axes.plot(t,y)

    def PlotInpInFrec(self,f,y):
        self.Inp_container =self.Axes.stem(f,y,basefmt='')
        self.Inp_is_in_plot=True

    def PlotFAA_InFrec(self,f,y):
        self.FAA_container= self.Axes.stem(f,y,basefmt='')
        self.FAA_is_in_plot= True

    def PlotSH_InFrec(self,f,y):
        self.SH_container= self.Axes.stem(f,y,basefmt='')
        self.SH_is_in_plot = True

    def PlotAnalogKey_InFrec(self,f,y):
        self.AnalogKey_container= self.Axes.stem(f,y,basefmt='')
        self.AnalogKey_is_in_plot = True

    def PlotOutput_InFrec(self,f,y):
        self.Output_container= self.Axes.stem(f,y,basefmt='')
        self.Output_is_in_plot = True

    def DisplaySelectedGraph(self,Xmin,Xmax,Ymin,Ymax,f,y_inp,y_faa,y_sh,y_key,y_out):
        sel = self.GetSelectedPlot()
        self.HideAllLines()
        self.Axes.grid(b=True,axis='both')
        self.Axes.set_axis_on()
        if(self.GetSelectedDomain() == TIME):
            if(sel== INPUT):
                self.Axes.set_xscale("linear")
                self.Axes.set_xlabel("t(seg)")
                self.Axes.set_ylabel("V(t) (Volts)")
                self.Axes.set_title("Xin(t)")
                self.Axes.set_xlim(left=Xmin,right=Xmax)
                if(Ymax ==float('NaN') or Ymax == float('inf') or Ymin ==float('NaN') or Ymin == float('inf')):
                    self.Axes.set_ylim(bottom=-100,top=100)
                else:
                    self.Axes.set_ylim(bottom=Ymin,top=Ymax)
                    self.Input_lines.set_visible(True) 
            elif(sel == A):
                self.Axes.set_xscale("linear")
                self.Axes.set_xlabel("t(seg)")
                self.Axes.set_ylabel("V(t) (Volts)")
                self.Axes.set_title("Nodo A(t)")
                self.Axes.set_xlim(left=Xmin,right=Xmax)
                if(Ymax ==float('NaN') or Ymax == float('inf') or Ymin ==float('NaN') or Ymin == float('inf') or Ymin == float('-inf')):
                    self.Axes.set_ylim(bottom=-100,top=100)
                else:
                    self.Axes.set_ylim(bottom=Ymin,top=Ymax)
                    self.NodeA_lines.set_visible(True)
            elif(sel == B):
                self.Axes.set_xscale("linear")
                self.Axes.set_xlabel("t(seg)")
                self.Axes.set_ylabel("V(t) (Volts)")
                self.Axes.set_title("Nodo B(t)")
                self.Axes.set_xlim(left=Xmin,right=Xmax)
                if(Ymax ==float('NaN') or Ymax == float('inf') or Ymin ==float('NaN') or Ymin == float('inf')):
                    self.Axes.set_ylim(bottom=-100,top=100)
                else:
                    self.Axes.set_ylim(bottom=Ymin,top=Ymax)
                    self.NodeB_lines.set_visible(True)
            elif(sel == C):
                self.Axes.set_xscale("linear")
                self.Axes.set_xlabel("t(seg)")
                self.Axes.set_ylabel("V(t) (Volts)")
                self.Axes.set_title("Nodo C(t)")
                self.Axes.set_xlim(left=Xmin,right=Xmax)
                if(Ymax ==float('NaN') or Ymax == float('inf') or Ymin ==float('NaN') or Ymin == float('inf')):
                    self.Axes.set_ylim(bottom=-100,top=100)
                else:
                    self.Axes.set_ylim(bottom=Ymin,top=Ymax)
                    self.NodeC_lines.set_visible(True)
            elif(sel == OUTPUT):
                self.Axes.set_xscale("linear")
                self.Axes.set_xlabel("t(seg)")
                self.Axes.set_ylabel("V(t) (Volts)")
                self.Axes.set_title("Xout(t)")
                self.Axes.set_xlim(left=Xmin,right=Xmax)
                if(Ymax ==float('NaN') or Ymax == float('inf') or Ymin ==float('NaN') or Ymin == float('inf')):
                    self.Axes.set_ylim(bottom=-100,top=100)
                else:
                    self.Axes.set_ylim(bottom=Ymin,top=Ymax)
                    self.Output_lines.set_visible(True)
        else:
            if(sel == INPUT):
                if(Ymax ==float('NaN') or Ymax == float('inf')):
                    self.Axes.set_xlim(left=Xmin,right=Xmax)
                    self.Axes.set_ylim(bottom=-100,top=100)
                    return
                else:
                    self.Axes.set_xlim(left=Xmin,right=Xmax)
                    self.Axes.set_ylim(bottom=Ymin,top=Ymax)
                self.Axes.set_xscale("linear")
                self.Axes.set_xlabel("f(Hz)")
                self.Axes.set_ylabel("|F{Xin(t)}|(f)")
                self.Axes.set_title("Harmonicos de Xin")
                self.Axes.set_xlim(left=Xmin,right=Xmax)
                self.Axes.set_ylim(bottom=Ymin,top=Ymax)
                self.PlotInpInFrec(f,y_inp)
            elif(sel == A):
                if(Ymax ==float('NaN') or Ymax == float('inf')):
                    self.Axes.set_xlim(left=Xmin,right=Xmax)
                    self.Axes.set_ylim(bottom=-100,top=100)
                    return
                else:
                    self.Axes.set_xlim(left=Xmin,right=Xmax)
                    self.Axes.set_ylim(bottom=Ymin,top=Ymax)
                self.Axes.set_xscale("linear")
                self.Axes.set_xlabel("f(Hz)")
                self.Axes.set_ylabel("|F{Va(t)}|(f)")
                self.Axes.set_title("Harmonicos de V(t) en A")
                self.Axes.set_xlim(left=Xmin,right=Xmax)
                self.Axes.set_ylim(bottom=Ymin,top=Ymax)
                self.PlotFAA_InFrec(f,y_faa)
            elif(sel == B):
                if(Ymax ==float('NaN') or Ymax == float('inf')):
                    self.Axes.set_xlim(left=Xmin,right=Xmax)
                    self.Axes.set_ylim(bottom=-100,top=100)
                    return
                else:
                    self.Axes.set_xlim(left=Xmin,right=Xmax)
                    self.Axes.set_ylim(bottom=Ymin,top=Ymax)
                self.Axes.set_xscale("linear")
                self.Axes.set_xlabel("f(Hz)")
                self.Axes.set_ylabel("|F{Vb(t)}|(f)")
                self.Axes.set_title("Harmonicos de V(t) en B")
                self.Axes.set_xlim(left=Xmin,right=Xmax)
                self.Axes.set_ylim(bottom=Ymin,top=Ymax)
                self.PlotSH_InFrec(f,y_sh)
            elif(sel == C):
                if(Ymax ==float('NaN') or Ymax == float('inf')):
                    self.Axes.set_xlim(left=Xmin,right=Xmax)
                    self.Axes.set_ylim(bottom=-100,top=100)
                    return
                else:
                    self.Axes.set_xlim(left=Xmin,right=Xmax)
                    self.Axes.set_ylim(bottom=Ymin,top=Ymax)
                self.Axes.set_xscale("linear")
                self.Axes.set_xlabel("f(Hz)")
                self.Axes.set_ylabel("|F{Vc(t)}|(f)")
                self.Axes.set_title("Harmonicos de V(t) en C")
                self.Axes.set_xlim(left=Xmin,right=Xmax)
                self.Axes.set_ylim(bottom=Ymin,top=Ymax)
                self.PlotAnalogKey_InFrec(f,y_key)
            elif(sel == OUTPUT):
                if(Ymax ==float('NaN') or Ymax == float('inf')):
                    self.Axes.set_xlim(left=Xmin,right=Xmax)
                    self.Axes.set_ylim(bottom=-100,top=100)
                    return
                else:
                    self.Axes.set_xlim(left=Xmin,right=Xmax)
                    self.Axes.set_ylim(bottom=Ymin,top=Ymax)
                self.Axes.set_xscale("linear")
                self.Axes.set_xlabel("f(Hz)")
                self.Axes.set_ylabel("|F{Xout(t)}|(f)")
                self.Axes.set_title("Harmonicos de Xout")
                self.Axes.set_xlim(left=Xmin,right=Xmax)
                self.Axes.set_ylim(bottom=Ymin,top=Ymax)
                self.PlotOutput_InFrec(f,y_out)
            

    #Callbacks

    def change_graph_button_call(self):
        self.Ev= PLOT_BUTTON_EV

    def change_domain_of_graph_call(self):
        self.Ev= TIME_FREQ_BUTTON_EV

    def input_change_callback(self,*args):
        self.input_changed = True
        self.Ev = INPUT_CHANGED_EV

    def selected_func_callback(self,*args):
        self.input_changed = True
        self.Ev = INPUT_CHANGED_EV
        if(self.selected_func.get() == "AM"):
            self.ShowingAmParameters= True
            self.InpFrecLabel.grid_forget() #Saco las entradas coresspondientes
            self.entry_inp_fo.grid_forget() #a otras funciones

            self.InpFpLabel.grid(row=1,column=0,sticky=W+E)        #Coloco las entradas correspondientes
            self.entry_inp_fp.grid(row=1,column=1,sticky=W+E,ipadx=110)   #a una funcion AM 
            self.InpFmLabel.grid(row=3,column=0,sticky=W+E)
            self.entry_inp_fm.grid(row=3,column=1,sticky=W+E)
            self.AmIndexLabel.grid(row=4,column=0,sticky=N+S+W+E)
            self.SlideAmIndex.grid(row=4,column=1,sticky=W+E)
        else:
            if(self.ShowingAmParameters):
                self.ShowingAmParameters = False
                self.InpFpLabel.grid_forget()       #Saco las entradas correspondientes
                self.entry_inp_fp.grid_forget()     #Correspondientes a una funcion AM
                self.InpFmLabel.grid_forget() 
                self.entry_inp_fm.grid_forget() 
                self.AmIndexLabel.grid_forget() 
                self.SlideAmIndex.grid_forget() 

                self.InpFrecLabel.grid(row=1,column=0,sticky=W+E)     #Pongo las entradas correspondientes
                self.entry_inp_fo.grid(row=1,column=1,sticky=W+E,ipadx=120)   #a las demas entradas

    def on_closing(self):
        if messagebox.askokcancel("Cerrar", "Desea cerrar el programa?"):
            self.Ev=QUIT_EV
    #Extras

    def CloseGUI(self):
        self.root.destroy()
    def Update(self):
        self.Graph.draw()
        self.root.update()
    def ShowMessage(self,string):
         messagebox.showinfo("",string)

    def EventSolved(self):
        self.Ev = NO_EV


