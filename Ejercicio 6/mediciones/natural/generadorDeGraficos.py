import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy.fftpack import fft, fftfreq
from mpldatacursor import datacursor


medCos7x5k = pd.read_csv("coseno/cos7x5k.csv")
medCos3k = pd.read_csv("coseno/cos3k.csv")
medCos20k = pd.read_csv("coseno/cos20k.csv")
med3sen7x5k = pd.read_csv("3medioSeno/3sen7x5k.csv")
med3sen20k = pd.read_csv("3medioSeno/3sen20k.csv")
med3sen500 = pd.read_csv("3medioSeno/3sen500hz.csv")
med3sen1000 = pd.read_csv("3medioSeno/3sen1000hz.csv")
med3sen3000 = pd.read_csv("3medioSeno/3sen3000hz.csv")
medCuad7x5k = pd.read_csv("cuadratica/cuad7x5k.csv")
medCuad20k = pd.read_csv("cuadratica/cuad20k.csv")
medCuad500 = pd.read_csv("cuadratica/cuad500hz.csv")
medCuad1000 = pd.read_csv("cuadratica/cuad1000hz.csv")
medCuad3000 = pd.read_csv("cuadratica/cuad3000hz.csv")






plt.figure(1) #GRAFICOS DE MEDICIONES COSENO EN TIEMPO
plt.subplot(1,4,1)
plt.plot(medCos7x5k["second"]+(1/1000), medCos7x5k["Volt2"], 'r', label='Nodo A')
plt.xlabel("t (seg)")
plt.ylabel("V(t) (Volts)")
plt.title("Nodo A(t)")
plt.grid(True)
plt.xticks()
plt.yticks()
plt.legend(loc = 'lower right')
datacursor(formatter="f:{x:.2f} Hz\n mag:{y:.2f} dB".format, display='multiple', draggable=True)

plt.subplot(1,4,2)
plt.plot(medCos7x5k["second"]+(1/1000), medCos7x5k["Volt3"], 'g', label='Nodo C')
plt.xlabel("t (seg)")
plt.ylabel("V(t) (Volts)")
plt.title("Nodo C(t)")
plt.grid(True)
plt.xticks()
plt.yticks()
plt.legend(loc = 'lower right')
datacursor(formatter="f:{x:.2f} Hz\n mag:{y:.2f} dB".format, display='multiple', draggable=True)

plt.subplot(1,4,3)
plt.plot(medCos7x5k["second"]+(1/1000), medCos7x5k["Volt1"], 'b', label='Xin(t)')
plt.xlabel("t (seg)")
plt.ylabel("V(t) (Volts)")
plt.title("Xin(t)")
plt.grid(True)
plt.xticks()
plt.yticks()
plt.legend(loc = 'lower right')
datacursor(formatter="f:{x:.2f} Hz\n mag:{y:.2f} dB".format, display='multiple', draggable=True)

plt.subplot(1,4,4)
plt.plot(medCos7x5k["second"]+(1/1000), medCos7x5k["Volt4"], 'm', label='Xout(t)')
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
plt.plot(med3sen7x5k["second"]+(1/1000), med3sen7x5k["Volt2"], 'r', label='Nodo A')
plt.xlabel("t (seg)")
plt.ylabel("V(t) (Volts)")
plt.title("Nodo A(t)")
plt.grid(True)
plt.xticks()
plt.yticks()
plt.legend(loc = 'lower right')
datacursor(formatter="f:{x:.2f} Hz\n mag:{y:.2f} dB".format, display='multiple', draggable=True)

plt.subplot(1,4,2)
plt.plot(med3sen7x5k["second"]+(1/1000), med3sen7x5k["Volt3"], 'g', label='Nodo C')
plt.xlabel("t (seg)")
plt.ylabel("V(t) (Volts)")
plt.title("Nodo C(t)")
plt.grid(True)
plt.xticks()
plt.yticks()
plt.legend(loc = 'lower right')
datacursor(formatter="f:{x:.2f} Hz\n mag:{y:.2f} dB".format, display='multiple', draggable=True)

plt.subplot(1,4,3)
plt.plot(med3sen7x5k["second"]+(1/1000), med3sen7x5k["Volt1"], 'b', label='Xin(t)')
plt.xlabel("t (seg)")
plt.ylabel("V(t) (Volts)")
plt.title("Xin(t)")
plt.grid(True)
plt.xticks()
plt.yticks()
plt.legend(loc = 'lower right')
datacursor(formatter="f:{x:.2f} Hz\n mag:{y:.2f} dB".format, display='multiple', draggable=True)

plt.subplot(1,4,4)
plt.plot(med3sen7x5k["second"]+(1/1000), med3sen7x5k["Volt4"], 'm', label='Xout(t)')
plt.xlabel("t (seg)")
plt.ylabel("V(t) (Volts)")
plt.title("Xout(t)")
plt.grid(True)
plt.xticks()
plt.yticks()
plt.legend(loc = 'lower right')
datacursor(formatter="f:{x:.2f} Hz\n mag:{y:.2f} dB".format, display='multiple', draggable=True)


plt.figure(3) #GRAFICOS DE MEDICIONES CUADRATICA EN TIEMPO
plt.subplot(1,4,1)
plt.plot(medCuad7x5k["second"]+(1/1000), medCuad7x5k["Volt2"], 'r', label='Nodo A')
plt.xlabel("t (seg)")
plt.ylabel("V(t) (Volts)")
plt.title("Nodo A(t)")
plt.grid(True)
plt.xticks()
plt.yticks()
plt.legend(loc = 'lower right')
datacursor(formatter="f:{x:.2f} Hz\n mag:{y:.2f} dB".format, display='multiple', draggable=True)

plt.subplot(1,4,2)
plt.plot(medCuad7x5k["second"]+(1/1000), medCuad7x5k["Volt3"], 'g', label='Nodo C')
plt.xlabel("t (seg)")
plt.ylabel("V(t) (Volts)")
plt.title("Nodo C(t)")
plt.grid(True)
plt.xticks()
plt.yticks()
plt.legend(loc = 'lower right')
datacursor(formatter="f:{x:.2f} Hz\n mag:{y:.2f} dB".format, display='multiple', draggable=True)

plt.subplot(1,4,3)
plt.plot(medCuad7x5k["second"]+(1/1000), medCuad7x5k["Volt1"], 'b', label='Xin(t)')
plt.xlabel("t (seg)")
plt.ylabel("V(t) (Volts)")
plt.title("Xin(t)")
plt.grid(True)
plt.xticks()
plt.yticks()
plt.legend(loc = 'lower right')
datacursor(formatter="f:{x:.2f} Hz\n mag:{y:.2f} dB".format, display='multiple', draggable=True)

plt.subplot(1,4,4)
plt.plot(medCuad7x5k["second"]+(1/1000), medCuad7x5k["Volt4"], 'm', label='Xout(t)')
plt.xlabel("t (seg)")
plt.ylabel("V(t) (Volts)")
plt.title("Xout(t)")
plt.grid(True)
plt.xticks()
plt.yticks()
plt.legend(loc = 'lower right')
datacursor(formatter="f:{x:.2f} Hz\n mag:{y:.2f} dB".format, display='multiple', draggable=True)





plt.figure(4) #GRAFICOS DE MEDICIONES COSENO EN TIEMPO
plt.subplot(1,4,1)
plt.plot(medCos3k["second"]+(1/1000), medCos3k["Volt2"], 'r', label='Nodo A')
plt.xlabel("t (seg)")
plt.ylabel("V(t) (Volts)")
plt.title("Nodo A(t)")
plt.grid(True)
plt.xticks()
plt.yticks()
plt.legend(loc = 'lower right')
datacursor(formatter="f:{x:.2f} Hz\n mag:{y:.2f} dB".format, display='multiple', draggable=True)

plt.subplot(1,4,2)
plt.plot(medCos3k["second"]+(1/1000), medCos3k["Volt3"], 'g', label='Nodo C')
plt.xlabel("t (seg)")
plt.ylabel("V(t) (Volts)")
plt.title("Nodo C(t)")
plt.grid(True)
plt.xticks()
plt.yticks()
plt.legend(loc = 'lower right')
datacursor(formatter="f:{x:.2f} Hz\n mag:{y:.2f} dB".format, display='multiple', draggable=True)

plt.subplot(1,4,3)
plt.plot(medCos3k["second"]+(1/1000), medCos3k["Volt1"], 'b', label='Xin(t)')
plt.xlabel("t (seg)")
plt.ylabel("V(t) (Volts)")
plt.title("Xin(t)")
plt.grid(True)
plt.xticks()
plt.yticks()
plt.legend(loc = 'lower right')
datacursor(formatter="f:{x:.2f} Hz\n mag:{y:.2f} dB".format, display='multiple', draggable=True)

plt.subplot(1,4,4)
plt.plot(medCos3k["second"]+(1/1000), medCos3k["Volt4"], 'm', label='Xout(t)')
plt.xlabel("t (seg)")
plt.ylabel("V(t) (Volts)")
plt.title("Xout(t)")
plt.grid(True)
plt.xticks()
plt.yticks()
plt.legend(loc = 'lower right')
datacursor(formatter="f:{x:.2f} Hz\n mag:{y:.2f} dB".format, display='multiple', draggable=True)



plt.figure(5) #GRAFICOS DE MEDICIONES COSENO EN TIEMPO
plt.subplot(1,4,1)
plt.plot(medCos20k["second"]+(1/1000), medCos20k["Volt2"], 'r', label='Nodo A')
plt.xlabel("t (seg)")
plt.ylabel("V(t) (Volts)")
plt.title("Nodo A(t)")
plt.grid(True)
plt.xticks()
plt.yticks()
plt.legend(loc = 'lower right')
datacursor(formatter="f:{x:.2f} Hz\n mag:{y:.2f} dB".format, display='multiple', draggable=True)

plt.subplot(1,4,2)
plt.plot(medCos20k["second"]+(1/1000), medCos20k["Volt3"], 'g', label='Nodo C')
plt.xlabel("t (seg)")
plt.ylabel("V(t) (Volts)")
plt.title("Nodo C(t)")
plt.grid(True)
plt.xticks()
plt.yticks()
plt.legend(loc = 'lower right')
datacursor(formatter="f:{x:.2f} Hz\n mag:{y:.2f} dB".format, display='multiple', draggable=True)

plt.subplot(1,4,3)
plt.plot(medCos20k["second"]+(1/1000), medCos20k["Volt1"], 'b', label='Xin(t)')
plt.xlabel("t (seg)")
plt.ylabel("V(t) (Volts)")
plt.title("Xin(t)")
plt.grid(True)
plt.xticks()
plt.yticks()
plt.legend(loc = 'lower right')
datacursor(formatter="f:{x:.2f} Hz\n mag:{y:.2f} dB".format, display='multiple', draggable=True)

plt.subplot(1,4,4)
plt.plot(medCos20k["second"]+(1/1000), medCos20k["Volt4"], 'm', label='Xout(t)')
plt.xlabel("t (seg)")
plt.ylabel("V(t) (Volts)")
plt.title("Xout(t)")
plt.grid(True)
plt.xticks()
plt.yticks()
plt.legend(loc = 'lower right')
datacursor(formatter="f:{x:.2f} Hz\n mag:{y:.2f} dB".format, display='multiple', draggable=True)



plt.figure(6) #GRAFICOS DE MEDICIONES 1.5 SENO EN TIEMPO
plt.subplot(1,4,1)
plt.plot(med3sen20k["second"]+(1/1000), med3sen20k["Volt2"], 'r', label='Nodo A')
plt.xlabel("t (seg)")
plt.ylabel("V(t) (Volts)")
plt.title("Nodo A(t)")
plt.grid(True)
plt.xticks()
plt.yticks()
plt.legend(loc = 'lower right')
datacursor(formatter="f:{x:.2f} Hz\n mag:{y:.2f} dB".format, display='multiple', draggable=True)

plt.subplot(1,4,2)
plt.plot(med3sen20k["second"]+(1/1000), med3sen20k["Volt3"], 'g', label='Nodo C')
plt.xlabel("t (seg)")
plt.ylabel("V(t) (Volts)")
plt.title("Nodo C(t)")
plt.grid(True)
plt.xticks()
plt.yticks()
plt.legend(loc = 'lower right')
datacursor(formatter="f:{x:.2f} Hz\n mag:{y:.2f} dB".format, display='multiple', draggable=True)

plt.subplot(1,4,3)
plt.plot(med3sen20k["second"]+(1/1000), med3sen20k["Volt1"], 'b', label='Xin(t)')
plt.xlabel("t (seg)")
plt.ylabel("V(t) (Volts)")
plt.title("Xin(t)")
plt.grid(True)
plt.xticks()
plt.yticks()
plt.legend(loc = 'lower right')
datacursor(formatter="f:{x:.2f} Hz\n mag:{y:.2f} dB".format, display='multiple', draggable=True)

plt.subplot(1,4,4)
plt.plot(med3sen20k["second"]+(1/1000), med3sen20k["Volt4"], 'm', label='Xout(t)')
plt.xlabel("t (seg)")
plt.ylabel("V(t) (Volts)")
plt.title("Xout(t)")
plt.grid(True)
plt.xticks()
plt.yticks()
plt.legend(loc = 'lower right')
datacursor(formatter="f:{x:.2f} Hz\n mag:{y:.2f} dB".format, display='multiple', draggable=True)


plt.figure(3) #GRAFICOS DE MEDICIONES CUADRATICA EN TIEMPO
plt.subplot(1,4,1)
plt.plot(medCuad20k["second"]+(1/1000), medCuad20k["Volt2"], 'r', label='Nodo A')
plt.xlabel("t (seg)")
plt.ylabel("V(t) (Volts)")
plt.title("Nodo A(t)")
plt.grid(True)
plt.xticks()
plt.yticks()
plt.legend(loc = 'lower right')
datacursor(formatter="f:{x:.2f} Hz\n mag:{y:.2f} dB".format, display='multiple', draggable=True)

plt.subplot(1,4,2)
plt.plot(medCuad20k["second"]+(1/1000), medCuad20k["Volt3"], 'g', label='Nodo C')
plt.xlabel("t (seg)")
plt.ylabel("V(t) (Volts)")
plt.title("Nodo C(t)")
plt.grid(True)
plt.xticks()
plt.yticks()
plt.legend(loc = 'lower right')
datacursor(formatter="f:{x:.2f} Hz\n mag:{y:.2f} dB".format, display='multiple', draggable=True)

plt.subplot(1,4,3)
plt.plot(medCuad20k["second"]+(1/1000), medCuad20k["Volt1"], 'b', label='Xin(t)')
plt.xlabel("t (seg)")
plt.ylabel("V(t) (Volts)")
plt.title("Xin(t)")
plt.grid(True)
plt.xticks()
plt.yticks()
plt.legend(loc = 'lower right')
datacursor(formatter="f:{x:.2f} Hz\n mag:{y:.2f} dB".format, display='multiple', draggable=True)

plt.subplot(1,4,4)
plt.plot(medCuad20k["second"]+(1/1000), medCuad20k["Volt4"], 'm', label='Xout(t)')
plt.xlabel("t (seg)")
plt.ylabel("V(t) (Volts)")
plt.title("Xout(t)")
plt.grid(True)
plt.xticks()
plt.yticks()
plt.legend(loc = 'lower right')
datacursor(formatter="f:{x:.2f} Hz\n mag:{y:.2f} dB".format, display='multiple', draggable=True)

plt.show()