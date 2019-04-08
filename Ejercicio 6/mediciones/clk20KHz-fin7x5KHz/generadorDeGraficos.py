import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from mpldatacursor import datacursor


medCosXin = pd.read_csv("muestreoCosenoXin.csv")
medCosXout = pd.read_csv("muestreoCosenoXout.csv")
medCosSHin = pd.read_csv("muestreoCosenoSHin.csv")
medCosSHout = pd.read_csv("muestreoCosenoSHout.csv")



plt.figure(1) #GRAFICOS DE MEDICIONES COSENO
plt.pyplot(meCosXin["second"], medCosXin["Volt"], label='Input')
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud (dB)")
plt.title("Medición x(t) ~ Coseno")
plt.grid(True)
plt.xticks()
plt.yticks()
plt.legend(loc = 'lower right')
datacursor(formatter="f:{x:.2f} Hz\n mag:{y:.2f} dB".format, display='multiple', draggable=True)


plt.show()