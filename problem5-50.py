# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 14:49:17 2019

@author: mrale
Find the Fourier coefficients an and bn for the function shown in Figure 5.28b
(Taylor - Classical Mechanics page 213). Make a plot comparing the function
itself with the first couple of terms in the Fourier series, and another for
the first 10 or so terms.
"""

import math
import matplotlib.pyplot as plt
import numpy as np


def sawtooth(t):
    t = t % 2
    f = np.zeros(np.shape(t))
    for i in range(0, len(t)):
        if t[i] < 1 :
            f[i] = t[i]
        else:
            f[i] = -2 + t[i]
    return f


def sawtooth_fourier(t, n):
    f = np.zeros(np.shape(t))
    for k in range(1, n):
        f = f + 2/math.pi*(-1)**(k - 1)/k*np.sin(k*math.pi*t)
    return f


t = np.linspace(-3, 3, 201)

plt.subplot(2, 1, 1)
plt.ylabel('f(t)')
plt.suptitle('Triangle function')
plt.title('3 terms of the Fourier-series')
plt.plot(t, sawtooth(t))
plt.plot(t, sawtooth_fourier(t, 3))
plt.xticks([])
plt.subplot(2, 1, 2)
plt.xlabel('t')
plt.ylabel('f(t)')
plt.title('11 terms of the Furier-series')
plt.plot(t, sawtooth_fourier(t, 11))

plt.show()
