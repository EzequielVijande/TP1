import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy.fftpack import fft, fftfreq
from mpldatacursor import datacursor
import funcGraf as graph


med = pd.read_csv("scope_36.csv")






plt.figure(1) #GRAFICOS DE MEDICIONES

graph.graficarSubplots(med["second"]+(5/1000), med["Volt1"], med["Volt2"], med["Volt3"], med["Volt4"])




plt.show()