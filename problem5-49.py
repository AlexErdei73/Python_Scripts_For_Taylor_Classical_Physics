# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 14:49:17 2019

@author: mrale
Find the Fourier coefficients an and bn for the function shown in Figure 5.28a
(Taylor - Classical Mechanics page 213). Make a plot comparing the function
itself with the first couple of terms in the Fourier series, and another for
the first six or so terms.
"""

import math
import matplotlib.pyplot as plt
import numpy as np


def triangle(t):
    t = t % 2
    f = np.zeros(np.shape(t))
    for i in range(0, len(t)):
        if t[i] < 1:
            f[i] = 1 - t[i]
        else:
            f[i] = -1 + t[i]
    return f


def triangle_fourier(t, n):
    f = np.zeros(np.shape(t))
    for i in range(0, len(t)):
        f[i] = 0.5
    for k in range(0, n):
        j = 2*k + 1
        f = f + 4/math.pi**2/j**2*np.cos(j*math.pi*t)
    return f


t = np.linspace(-3, 3, 201)

plt.subplot(2, 1, 1)
plt.ylabel('f(t)')
plt.suptitle('Triangle function')
plt.title('2 terms of the Fourier-series')
plt.plot(t, triangle(t))
plt.plot(t, triangle_fourier(t, 1))
plt.xticks([])
plt.subplot(2, 1, 2)
plt.xlabel('t')
plt.ylabel('f(t)')
plt.title('7 terms of the Furier-series')
plt.plot(t, triangle_fourier(t, 6))

plt.show()
