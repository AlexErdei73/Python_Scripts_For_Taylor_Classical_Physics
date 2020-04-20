# -*- coding: utf-8 -*-
"""
Created on Tue Mar 05 13:48:07 2019

@author: mrale
Make a plot of x(t) for a driven damped linear oscillator, wich is released
from rest at the x0=0 position at time t=0, with the following parameters:
Drive frequency omega=2*pi, natural frequency omega0=5*omega, decay constant
beta=omega0/20, and driving amplitude f0=1000. Show the first 5 cycles.
X(t) is the solution of the following differential equation:

    x''(t) + 2*beta*x'(t) + omega0**2*x(t) = f0*cos(omega*t)

"""

import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.integrate import solve_ivp

x0 = 0
v0 = 0
omega = 2*math.pi
omega0 = 5*omega
beta = omega0/20.0
f0 = 1000
t = np.linspace(0, 4, 201)


def dydt(t, y):
    x, v = y
    return (v, -2*beta*v - omega0**2*x + f0*math.cos(omega*t))


sol = solve_ivp(dydt, [0, 4], [x0, v0], t_eval=t)
y = sol.y

plt.subplot(2, 1, 1)
plt.suptitle('Driven Damped Oscillator')
plt.ylabel('f(t)')
plt.xticks([])
plt.title('driving force')
plt.plot(t, f0*np.cos(omega*t))
plt.subplot(2, 1, 2)
plt.ylabel('x(t)')
plt.xlabel('t(s)')
plt.title('resulting motion')
plt.plot(t, y[0, :])

plt.show()
