import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from mpldatacursor import datacursor


medCosXin = pd.read_csv("muestreoCosenoXin.csv")
medCosXout = pd.read_csv("muestreoCosenoXout.csv")



plt.figure(1) #GRAFICOS DE MEDICIONES COSENO
plt.subplot(1,4,1)
plt.plot(medCosXin["second"], medCosXin["Volt"], 'r', label='Nodo A')
plt.xlabel("t (seg)")
plt.ylabel("V(t) (Volts)")
plt.title("Nodo A(t)")
plt.grid(True)
plt.xticks()
plt.yticks()
plt.legend(loc = 'lower right')
datacursor(formatter="f:{x:.2f} Hz\n mag:{y:.2f} dB".format, display='multiple', draggable=True)

plt.subplot(1,4,2)
plt.plot(medCosXin["second"], medCosXin["Volt"], 'g', label='Nodo C')
plt.xlabel("t (seg)")
plt.ylabel("V(t) (Volts)")
plt.title("Nodo C(t)")
plt.grid(True)
plt.xticks()
plt.yticks()
plt.legend(loc = 'lower right')
datacursor(formatter="f:{x:.2f} Hz\n mag:{y:.2f} dB".format, display='multiple', draggable=True)

plt.subplot(1,4,3)
plt.plot(medCosXin["second"], medCosXin["Volt"], 'b', label='Xin(t)')
plt.xlabel("t (seg)")
plt.ylabel("V(t) (Volts)")
plt.title("Xin(t)")
plt.grid(True)
plt.xticks()
plt.yticks()
plt.legend(loc = 'lower right')
datacursor(formatter="f:{x:.2f} Hz\n mag:{y:.2f} dB".format, display='multiple', draggable=True)

plt.subplot(1,4,4)
plt.plot(medCosXin["second"], medCosXin["Volt"], 'm', label='Xout(t)')
plt.xlabel("t (seg)")
plt.ylabel("V(t) (Volts)")
plt.title("Xout(t)")
plt.grid(True)
plt.xticks()
plt.yticks()
plt.legend(loc = 'lower right')
datacursor(formatter="f:{x:.2f} Hz\n mag:{y:.2f} dB".format, display='multiple', draggable=True)


plt.show()