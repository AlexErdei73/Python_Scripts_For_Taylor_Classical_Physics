# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 10:38:46 2019

@author: mrale

Plot the U(fi)=-mgRfi+MgR(1-cos(fi)) function
for m=0.7M and m=0.8M case
"""

import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve


def U(fi, m, M, R):
    g = 9.81
    return -m*g*R*fi + M*g*R*(1 - np.cos(fi))


fi = np.linspace(0, 4, 100)
plt.plot(fi, U(fi, 0.7, 1, 1))
plt.plot(fi, U(fi, 0.8, 1, 1))
plt.show()


def Umax(m):
    R = 1
    M = 1
    fimax = math.pi - math.asin(m/M)
    return U(fimax, m, M, R)


mlimit = fsolve(Umax, 0.7)
print 'The limit of oscillation for m/M = %5.3f' % mlimit
