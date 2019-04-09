import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy.fftpack import fft, fftfreq
from mpldatacursor import datacursor
import funcGraf as graph


medCos7x5k = pd.read_csv("coseno/cos7x5k.csv")
medCos3k = pd.read_csv("coseno/cos3k.csv")
medCos20k = pd.read_csv("coseno/cos20k.csv")
med3sen7x5k = pd.read_csv("3medioSeno/3sen7x5k.csv")
med3sen20k = pd.read_csv("3medioSeno/3sen20k.csv")
med3sen500hz = pd.read_csv("3medioSeno/3sen500hz.csv")
med3sen1000hz = pd.read_csv("3medioSeno/3sen1000hz.csv")
med3sen3000hz = pd.read_csv("3medioSeno/3sen3000hz.csv")
medCuad7x5k = pd.read_csv("cuadratica/cuad7x5k.csv")
medCuad20k = pd.read_csv("cuadratica/cuad20k.csv")
medCuad500hz = pd.read_csv("cuadratica/cuad500hz.csv")
medCuad1000hz = pd.read_csv("cuadratica/cuad1000hz.csv")
medCuad3000hz = pd.read_csv("cuadratica/cuad3000hz.csv")






plt.figure(1) #GRAFICOS DE MEDICIONES

graph.graficarSubplots(medCos3k["second"]+(5/1000), medCos3k["Volt1"], medCos3k["Volt2"], medCos3k["Volt3"], medCos3k["Volt4"])

plt.figure(2) #GRAFICOS DE MEDICIONES

graph.graficarSubplots(medCos7x5k["second"]+(1/1000), medCos7x5k["Volt1"], medCos7x5k["Volt2"], medCos7x5k["Volt3"], medCos7x5k["Volt4"])

plt.figure(3) #GRAFICOS DE MEDICIONES

graph.graficarSubplots(medCos20k["second"]+(1/10000), medCos20k["Volt1"], medCos20k["Volt2"], medCos20k["Volt3"], medCos20k["Volt4"])

plt.figure(4) #GRAFICOS DE MEDICIONES

graph.graficarSubplots(med3sen7x5k["second"]+(1/100), med3sen7x5k["Volt1"], med3sen7x5k["Volt2"], med3sen7x5k["Volt3"], med3sen7x5k["Volt4"])

plt.figure(5) #GRAFICOS DE MEDICIONES

graph.graficarSubplots(med3sen20k["second"]+(1/100), med3sen20k["Volt1"], med3sen20k["Volt2"], med3sen20k["Volt3"], med3sen20k["Volt4"])

plt.figure(6) #GRAFICOS DE MEDICIONES

graph.graficarSubplots(med3sen500hz["second"]+(1/250), med3sen500hz["Volt1"], med3sen500hz["Volt2"], med3sen500hz["Volt3"], med3sen500hz["Volt4"])


plt.figure(7) #GRAFICOS DE MEDICIONES

graph.graficarSubplots(med3sen1000hz["second"]+(1/1000), med3sen1000hz["Volt1"], med3sen1000hz["Volt2"], med3sen1000hz["Volt3"], med3sen1000hz["Volt4"])

plt.figure(8) #GRAFICOS DE MEDICIONES

graph.graficarSubplots(med3sen3000hz["second"]+(1/3000), med3sen3000hz["Volt1"], med3sen3000hz["Volt2"], med3sen3000hz["Volt3"], med3sen3000hz["Volt4"])


plt.figure(9) #GRAFICOS DE MEDICIONES

graph.graficarSubplots(medCuad7x5k["second"]+(1/800), medCuad7x5k["Volt1"], medCuad7x5k["Volt2"], medCuad7x5k["Volt3"], medCuad7x5k["Volt4"])

plt.figure(10) #GRAFICOS DE MEDICIONES

graph.graficarSubplots(medCuad20k["second"]+(1/25000), medCuad20k["Volt1"], medCuad20k["Volt2"], medCuad20k["Volt3"], medCuad20k["Volt4"])

plt.figure(11) #GRAFICOS DE MEDICIONES

graph.graficarSubplots(medCuad500hz["second"]+(1/250), medCuad500hz["Volt1"], medCuad500hz["Volt2"], medCuad500hz["Volt3"], medCuad500hz["Volt4"])


plt.figure(12) #GRAFICOS DE MEDICIONES

graph.graficarSubplots(medCuad1000hz["second"]+(1/1000), medCuad1000hz["Volt1"], medCuad1000hz["Volt2"], medCuad1000hz["Volt3"], medCuad1000hz["Volt4"])

plt.figure(13) #GRAFICOS DE MEDICIONES

graph.graficarSubplots(medCuad3000hz["second"]+(1/3000), medCuad3000hz["Volt1"], medCuad3000hz["Volt2"], medCuad3000hz["Volt3"], medCuad3000hz["Volt4"])



plt.show()