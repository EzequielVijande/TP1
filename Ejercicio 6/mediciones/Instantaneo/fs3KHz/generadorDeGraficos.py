import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy.fftpack import fft, fftfreq
from mpldatacursor import datacursor


medCosXin = pd.read_csv("muestreoCosXin.csv")
medCosXout = pd.read_csv("muestreoCosXout.csv")
medCosSHin = pd.read_csv("muestreoCosSHin.csv")
medCosSHout = pd.read_csv("muestreoCosSHout.csv")






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

plt.title("Nodo C(t)")
plt.grid(True)
plt.xticks()
plt.yticks()
plt.legend(loc = 'lower right')
datacursor(formatter="f:{x:.2f} Hz\n mag:{y:.2f} dB".format, display='multiple', draggable=True)

plt.subplot(1,4,3)
plt.plot(medCosXin["second"]+(1/1000), medCosXin["Volt"], 'b', label='Xin(t)')
plt.xlabel("t (seg)")

plt.title("Xin(t)")
plt.grid(True)
plt.xticks()
plt.yticks()
plt.legend(loc = 'lower right')
datacursor(formatter="f:{x:.2f} Hz\n mag:{y:.2f} dB".format, display='multiple', draggable=True)

plt.subplot(1,4,4)
plt.plot(medCosXout["second"]+(1/1000), medCosXout["Volt"], 'm', label='Xout(t)')
plt.xlabel("t (seg)")

plt.title("Xout(t)")
plt.grid(True)
plt.xticks()
plt.yticks()
plt.legend(loc = 'lower right')
datacursor(formatter="f:{x:.2f} Hz\n mag:{y:.2f} dB".format, display='multiple', draggable=True)



plt.show()