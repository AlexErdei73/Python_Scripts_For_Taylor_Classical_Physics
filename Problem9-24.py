# -*- coding: utf-8 -*-
"""
Created on Fri May 17 14:27:02 2019

@author: mrale
Use a suitable plotting program to plot the orbits of the puck of Problem 9.20
on a rotating turntable with x0=Omega=1 and the following initial velocities:
v0: (0, 1), (0, 0), (0, -1), (-0.5, -0.5), (-0.7, -0.7), (0, -0.1)
"""

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 6.3, 201)
allv0 = [[0, 1], [0, 0], [0, -1], [-0.5, -0.5], [-0.7, -0.7], [0, -0.1]]
x0 = 1
Omega = 1

Fi = Omega*t

for v0 in allv0:
    x = (x0 + v0[0]*t)*np.cos(Fi) + (v0[1] + Omega*x0)*t*np.sin(Fi)
    y = -(x0 + v0[0]*t)*np.sin(Fi) + (v0[1] + Omega*x0)*t*np.cos(Fi)
    line = 'v0=' + str(v0)
    print(line)
    plt.plot(x, y)
    plt.grid()
    plt.show()
    print
    print
