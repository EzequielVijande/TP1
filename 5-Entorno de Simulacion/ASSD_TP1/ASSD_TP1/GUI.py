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
GRAPH_BUTTON_EV=2

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
    "cuadrada"
    ]
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

        #Botones para cambiar de graficas
        self.SelectedGraph= tk.IntVar()
        self.GraphButtonFrame = Frame(master=self.PlotFrame)
        self.GraphButtonFrame.grid(row=2)
        self.TimeButton= Radiobutton(master=self.GraphButtonFrame,text="En tiempo",background=GRAPH_BUTTON_COLOR,fg=GRAPH_BUTTON_TEXT_COLOR,
                                     indicatoron=False,variable=self.SelectedGraph,value=TIME,command=self.change_graph_button_call)
        self.TimeButton.grid(row=0,column=0,sticky=W+E)
        self.FreqButton= Radiobutton(master=self.GraphButtonFrame,text="En frecuencia",background=GRAPH_BUTTON_COLOR,fg=GRAPH_BUTTON_TEXT_COLOR,
                                     indicatoron=False,variable=self.SelectedGraph,value=FREQ,command=self.change_graph_button_call)
        self.FreqButton.grid(row=0,column=1,sticky=W+E)

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

        self.InpAmpLabel= Label(master=self.InputFrame,text="Amp(V)",anchor=W,background=BUTTON_COLOR,fg=BUTTON_FONT_COLOR)
        self.InpAmpLabel.grid(row=2,column=0,sticky=W+E)
        self.entry_inp_amp= Entry(master=self.InputFrame,textvariable=self.InpAmpString)
        self.entry_inp_amp.grid(row=2,column=1,sticky=W+E)


    def CreateFilterSection(self):
        self.FilterFcString= StringVar()
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
        self.FAA_BypassButton= Checkbutton(master=self.FilterFrame, text="Bypass FAA",
                        variable=self.BypassFAA,onvalue=BYPASS_ON, offvalue=BYPASS_OFF,background=BUTTON_COLOR,fg=BUTTON_FONT_COLOR)
        self.FAA_BypassButton.grid(row=1,column=0,sticky=W+E)
        self.FR_BypassButton= Checkbutton(master=self.FilterFrame, text="Bypass FR",
                        variable=self.BypassFR,onvalue=BYPASS_ON, offvalue=BYPASS_OFF,background=BUTTON_COLOR,fg=BUTTON_FONT_COLOR)
        self.FR_BypassButton.grid(row=1,column=1,sticky=W+E)
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
        self.entry_sampler_fs= Entry(master=self.SamplerFrame,textvariable=self.FilterFcString)
        self.entry_sampler_fs.grid(row=0,column=1,sticky=W+E,ipadx=70)
        #Duty cycle
        self.SlideDC_Label = Label(master=self.SamplerFrame,text="DC(%)",anchor=W,background=BUTTON_COLOR,fg=BUTTON_FONT_COLOR)
        self.SlideDC_Label.grid(row=1,column=0,sticky=N+S+W+E)
        self.SlideDC = Scale(master=self.SamplerFrame, from_=0, to=100,orient=HORIZONTAL)
        self.SlideDC.config(bg=BUTTON_COLOR)
        self.SlideDC.grid(row=1,column=1,sticky=W+E,ipadx=120)
        #Botones de Bypass
        self.SH_BypassButton= Checkbutton(master=self.SamplerFrame, text="Bypass SH",
                        variable=self.BypassSH,onvalue=BYPASS_ON, offvalue=BYPASS_OFF,background=BUTTON_COLOR,fg=BUTTON_FONT_COLOR)
        self.SH_BypassButton.grid(row=2,column=0,sticky=W+E)
        self.KEY_BypassButton= Checkbutton(master=self.SamplerFrame, text="Bypass Key",
                        variable=self.BypassKey,onvalue=BYPASS_ON, offvalue=BYPASS_OFF,background=BUTTON_COLOR,fg=BUTTON_FONT_COLOR)
        self.KEY_BypassButton.grid(row=2,column=1,sticky=W+E)


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

    #Callbacks

    def change_graph_button_call(self):
        self.Ev= GRAPH_BUTTON_EV

    def on_closing(self):
        if messagebox.askokcancel("Cerrar", "Desea cerrar el programa?"):
            self.Ev=QUIT_EV
    #Extras

    def CloseGUI(self):
        self.root.destroy()
    def Update(self):
        self.root.update()
    def EventSolved(self):
        self.Ev = NO_EV

