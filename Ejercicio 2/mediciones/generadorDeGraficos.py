import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from mpldatacursor import datacursor


medBodeFAA = pd.read_csv("bodeFAA.csv")
medBodeFR = pd.read_csv("bodeFR.csv")



plt.figure(1) #GRAFICO DE MAGNITUD medBodeFAA y medBode FR
plt.semilogx(medBodeFAA["f"], medBodeFAA["mag"], label='Filtro Antialiasing')
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud (dB)")
plt.title("Diagramas de Bode Filtros FAA y FR - Magnitud")
plt.grid(True)
plt.semilogx(medBodeFAA["f"], medBodeFR["mag"], label='Filtro Recuperador')
plt.xticks()
plt.yticks()
plt.legend(loc = 'lower right')
datacursor(formatter="f:{x:.2f} Hz\n mag:{y:.2f} dB".format, display='multiple', draggable=True)


plt.show()