import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy.fftpack import fft, fftfreq
from mpldatacursor import datacursor


def graficarSubplots(t, v1, v2, v3, v4):
    plt.subplot(1,4,1)
    plt.plot(t, v2, 'r', label='Nodo A')
    plt.xlabel("t (seg)")
    plt.ylabel("V(t) (Volts)")
    plt.title("Nodo A(t)")
    plt.grid(True)
    plt.xticks()
    plt.yticks()
    plt.legend(loc = 'lower right')
    datacursor(formatter="f:{x:.2f} Hz\n mag:{y:.2f} dB".format, display='multiple', draggable=True)

    plt.subplot(1,4,2)
    plt.plot(t, v3, 'g', label='Nodo C')
    plt.xlabel("t (seg)")
   
    plt.title("Nodo C(t)")
    plt.grid(True)
    plt.xticks()
    plt.yticks()
    plt.legend(loc = 'lower right')
    datacursor(formatter="f:{x:.2f} Hz\n mag:{y:.2f} dB".format, display='multiple', draggable=True)

    plt.subplot(1,4,3)
    plt.plot(t, v1, 'b', label='Xin(t)')
    plt.xlabel("t (seg)")
    
    plt.title("Xin(t)")
    plt.grid(True) 
    plt.xticks()
    plt.yticks()
    plt.legend(loc = 'lower right')
    datacursor(formatter="f:{x:.2f} Hz\n mag:{y:.2f} dB".format, display='multiple', draggable=True)

    plt.subplot(1,4,4)
    plt.plot(t, v4, 'm', label='Xout(t)')
    plt.xlabel("t (seg)")
   
    plt.title("Xout(t)")
    plt.grid(True)
    plt.xticks()
    plt.yticks()
    plt.legend(loc = 'lower right')
    datacursor(formatter="f:{x:.2f} Hz\n mag:{y:.2f} dB".format, display='multiple', draggable=True)




