import math
import numpy

from matplotlib import pyplot as p


# #################################
# #########decimate################
# #################################
# decimate decimates a given sequence:
# It takes a sequence x and an integer m
# and returns a sequence y, with y = x(n*m)
#
# INPUT:
#       1) x: sequence to be decimated. Should be centered in 0, so that x[0]
#               is the sequence x on time n0 = - len(x)//2 (x(n0) = x[0])
#       2) m: integer used to perform the decimation. The return array will
#
# OUTPUT:   a list containing, in order:
#       1) new_n : a list containing the values of n for which y is not null.
#              new_n should be used to plot the returned y when its plot will be superposed with x.
#              In this way, y will show the samples that were taken from x.
#              In other words, new_ n = n*m
#       2) real_n : a list containing the values of m*n, for which y is not null.
#                real_n should be used to plot y as a new sequence.
#                It can be used to compare the time differences of x vs. y.
#                In other words, real_n = n
#       3) y : Decimation of x: List of values of the x sequence that were taken when performing
#               x scaling by m. y(n) = x(n*m) (real_n = n)


def decimate(x, m, n=None, plotea=False, real_n_plot=False):
    y = []
    new_n = []
    real_n = []

    abs_m = abs(m)
    if abs_m >= 1:
        for i in range(0, len(x) // abs_m):
            y.append(x[(len(x)//2) % abs_m + i * abs_m])
        if m < 0:
            y.reverse()

        new_n = list(range(-(len(x) // 2 // abs_m) * abs_m, (len(x) // 2 // abs_m) * abs_m + 1, abs_m))
        real_n = list(range(-len(x) // abs_m // 2, len(x) // 2 // abs_m))

        for i in range(len(y)):
            if abs(y[i]) <= 1e-14:
                y[i] = 0
        if plotea:

            if real_n_plot:
                p.grid(True)
                p.stem(real_n, y)
                p.show()
            else:
                p.plot(n, x)
                p.stem(new_n, y)
                p.show()

        freq = numpy.fft.fftfreq(len(n))
        numpy.ndarray.sort(freq)
        p.plot(freq, abs(numpy.fft.fft(x)))

        freq_prima = numpy.fft.fftfreq(len(real_n))
        numpy.ndarray.sort(freq_prima)
        p.plot(freq_prima, abs(numpy.fft.fft(y)))
        p.title('X2(f) sin decimar y decimado')
        p.xlabel('Frecuencia f')
        p.ylabel('X2(f) y X2(f) decimado')

        p.show()
    else:
        print("Error. Ingreso un  valor no entero para efectuar la decimation!")

    return [new_n, real_n, y]


# original time vector for both x1 and x2
n = list(range(-50, 51, 1))

x1 = [numpy.sin(2*math.pi*0.125/2*n[i]) for i in range(len(n))]
decimate(x1, 4, n, True, False)

x2 = [numpy.sin(2*math.pi*0.25*n[i]) for i in range(len(n))]
decimate(x2, 4, n, True, True)


