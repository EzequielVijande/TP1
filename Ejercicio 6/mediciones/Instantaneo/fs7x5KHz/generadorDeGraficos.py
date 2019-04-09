import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy.fftpack import fft, fftfreq
from mpldatacursor import datacursor


medCosXin = pd.read_csv("muestreoCosenoXin.csv")
medCosXout = pd.read_csv("muestreoCosenoXout.csv")
medCosSHin = pd.read_csv("muestreoCosenoSHin.csv")
medCosSHout = pd.read_csv("muestreoCosenoSHout.csv")
med3senXin = pd.read_csv("muestreo3senXin.csv")
med3senXout = pd.read_csv("muestreo3senXout.csv")
med3senSHin = pd.read_csv("muestreo3senSHin.csv")
med3senSHout = pd.read_csv("muestreo3senSHout.csv")
medCuadXin = pd.read_csv("muestreoCuadXin.csv")
medCuadXout = pd.read_csv("muestreoCuadXout.csv")
medCuadSHin = pd.read_csv("muestreoCuadSHin.csv")
medCuadSHout = pd.read_csv("muestreoCuadSHout.csv")






plt.figure(1) #GRAFICOS DE MEDICIONES COSENO EN TIEMPO
plt.subplot(1,4,1)
plt.plot(medCosSHin["second"]+(1/1000), medCosSHin["Volt"], 'r', label='Nodo A')
plt.xlabel("t (seg)")
plt.ylabel("V(t) (Volts)")
plt.title("Nodo A(t)")
plt.grid(True)
plt.xticks()
plt.yticks()
plt.legend(loc = 'lower right')
datacursor(formatter="f:{x:.2f} Hz\n mag:{y:.2f} dB".format, display='multiple', draggable=True)

plt.subplot(1,4,2)
plt.plot(medCosSHout["second"]+(1/1000), medCosSHout["Volt"], 'g', label='Nodo C')
plt.xlabel("t (seg)")
plt.ylabel("V(t) (Volts)")
plt.title("Nodo C(t)")
plt.grid(True)
plt.xticks()
plt.yticks()
plt.legend(loc = 'lower right')
datacursor(formatter="f:{x:.2f} Hz\n mag:{y:.2f} dB".format, display='multiple', draggable=True)

plt.subplot(1,4,3)
plt.plot(medCosXin["second"]+(1/1000), medCosXin["Volt"], 'b', label='Xin(t)')
plt.xlabel("t (seg)")
plt.ylabel("V(t) (Volts)")
plt.title("Xin(t)")
plt.grid(True)
plt.xticks()
plt.yticks()
plt.legend(loc = 'lower right')
datacursor(formatter="f:{x:.2f} Hz\n mag:{y:.2f} dB".format, display='multiple', draggable=True)

plt.subplot(1,4,4)
plt.plot(medCosXout["second"]+(1/1000), medCosXout["Volt"], 'm', label='Xout(t)')
plt.xlabel("t (seg)")
plt.ylabel("V(t) (Volts)")
plt.title("Xout(t)")
plt.grid(True)
plt.xticks()
plt.yticks()
plt.legend(loc = 'lower right')
datacursor(formatter="f:{x:.2f} Hz\n mag:{y:.2f} dB".format, display='multiple', draggable=True)



plt.figure(2) #GRAFICOS DE MEDICIONES 1.5 SENO EN TIEMPO
plt.subplot(1,4,1)
plt.plot(med3senSHin["second"]+(1/1000), med3senSHin["Volt"], 'r', label='Nodo A')
plt.xlabel("t (seg)")
plt.ylabel("V(t) (Volts)")
plt.title("Nodo A(t)")
plt.grid(True)
plt.xticks()
plt.yticks()
plt.legend(loc = 'lower right')
datacursor(formatter="f:{x:.2f} Hz\n mag:{y:.2f} dB".format, display='multiple', draggable=True)

plt.subplot(1,4,2)
plt.plot(med3senSHout["second"]+(1/1000), med3senSHout["Volt"], 'g', label='Nodo C')
plt.xlabel("t (seg)")

plt.title("Nodo C(t)")
plt.grid(True)
plt.xticks()
plt.yticks()
plt.legend(loc = 'lower right')
datacursor(formatter="f:{x:.2f} Hz\n mag:{y:.2f} dB".format, display='multiple', draggable=True)

plt.subplot(1,4,3)
plt.plot(med3senXin["second"]+(1/1000), med3senXin["Volt"], 'b', label='Xin(t)')
plt.xlabel("t (seg)")

plt.title("Xin(t)")
plt.grid(True)
plt.xticks()
plt.yticks()
plt.legend(loc = 'lower right')
datacursor(formatter="f:{x:.2f} Hz\n mag:{y:.2f} dB".format, display='multiple', draggable=True)

plt.subplot(1,4,4)
plt.plot(med3senXout["second"]+(1/1000), med3senXout["Volt"], 'm', label='Xout(t)')
plt.xlabel("t (seg)")

plt.title("Xout(t)")
plt.grid(True)
plt.xticks()
plt.yticks()
plt.legend(loc = 'lower right')
datacursor(formatter="f:{x:.2f} Hz\n mag:{y:.2f} dB".format, display='multiple', draggable=True)


plt.figure(3) #GRAFICOS DE MEDICIONES CUADRATICA EN TIEMPO
plt.subplot(1,4,1)
plt.plot(medCuadSHin["second"]+(1/1000), medCuadSHin["Volt"], 'r', label='Nodo A')
plt.xlabel("t (seg)")
plt.ylabel("V(t) (Volts)")
plt.title("Nodo A(t)")
plt.grid(True)
plt.xticks()
plt.yticks()
plt.legend(loc = 'lower right')
datacursor(formatter="f:{x:.2f} Hz\n mag:{y:.2f} dB".format, display='multiple', draggable=True)

plt.subplot(1,4,2)
plt.plot(medCuadSHout["second"]+(1/1000), medCuadSHout["Volt"], 'g', label='Nodo C')
plt.xlabel("t (seg)")

plt.title("Nodo C(t)")
plt.grid(True)
plt.xticks()
plt.yticks()
plt.legend(loc = 'lower right')
datacursor(formatter="f:{x:.2f} Hz\n mag:{y:.2f} dB".format, display='multiple', draggable=True)

plt.subplot(1,4,3)
plt.plot(medCuadXin["second"]+(1/1000), medCuadXin["Volt"], 'b', label='Xin(t)')
plt.xlabel("t (seg)")

plt.title("Xin(t)")
plt.grid(True)
plt.xticks()
plt.yticks()
plt.legend(loc = 'lower right')
datacursor(formatter="f:{x:.2f} Hz\n mag:{y:.2f} dB".format, display='multiple', draggable=True)

plt.subplot(1,4,4)
plt.plot(medCuadXout["second"]+(1/1000), medCuadXout["Volt"], 'm', label='Xout(t)')
plt.xlabel("t (seg)")

plt.title("Xout(t)")
plt.grid(True)
plt.xticks()
plt.yticks()
plt.legend(loc = 'lower right')
datacursor(formatter="f:{x:.2f} Hz\n mag:{y:.2f} dB".format, display='multiple', draggable=True)

plt.show()