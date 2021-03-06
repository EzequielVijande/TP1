import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from mpldatacursor import datacursor


medCosXin = pd.read_csv("muestreoCosenoXin.csv")
medCosXout = pd.read_csv("muestreoCosenoXout.csv")
med3senXin = pd.read_csv("muestreo3senfXin.csv")
med3senXout = pd.read_csv("muestreo3senfXout.csv")



plt.figure(1) #GRAFICOS DE MEDICIONES COSENO
plt.subplot(1,2,1)
plt.plot(medCosXin["second"], medCosXin["Volt"], 'r', label='Nodo A')
plt.xlabel("t (seg)")
plt.ylabel("V(t) (Volts)")
plt.title("Nodo A(t)")
plt.grid(True)
plt.xticks()
plt.yticks()
plt.legend(loc = 'lower right')
datacursor(formatter="f:{x:.2f} Hz\n mag:{y:.2f} dB".format, display='multiple', draggable=True)

plt.subplot(1,2,2)
plt.plot(medCosXout["second"], medCosXout["Volt"], 'g', label='Nodo C')
plt.xlabel("t (seg)")
plt.title("Nodo C(t)")
plt.grid(True)
plt.xticks()
plt.yticks()
plt.legend(loc = 'lower right')
datacursor(formatter="f:{x:.2f} Hz\n mag:{y:.2f} dB".format, display='multiple', draggable=True)


plt.figure(2) #GRAFICOS DE MEDICIONES COSENO
plt.subplot(1,2,1)
plt.plot(med3senXin["second"], med3senXin["Volt"], 'r', label='Nodo A')
plt.xlabel("t (seg)")
plt.ylabel("V(t) (Volts)")
plt.title("Nodo A(t)")
plt.grid(True)
plt.xticks()
plt.yticks()
plt.legend(loc = 'lower right')
datacursor(formatter="f:{x:.2f} Hz\n mag:{y:.2f} dB".format, display='multiple', draggable=True)

plt.subplot(1,2,2)
plt.plot(med3senXout["second"], med3senXout["Volt"], 'g', label='Nodo C')
plt.xlabel("t (seg)")
plt.title("Nodo C(t)")
plt.grid(True)
plt.xticks()
plt.yticks()
plt.legend(loc = 'lower right')
datacursor(formatter="f:{x:.2f} Hz\n mag:{y:.2f} dB".format, display='multiple', draggable=True)



plt.show()