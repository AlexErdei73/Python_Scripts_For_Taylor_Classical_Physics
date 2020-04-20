# -*- coding: utf-8 -*-
"""
Created on Tue Mar 05 13:48:07 2019

@author: mrale
Make a plot of x(t) for a driven damped linear oscillator, wich is released
from rest at the x0=2 position at time t=0, with the following parameters:
Drive frequency omega=2*pi, natural frequency omega0=5*omega, decay constant
beta=omega0/20, and driving amplitude f0=1000. Show the first 5 cycles.

x(t) = A*cos(omega*t - delta) +
    exp(-beta*t)*[B1*cos(omega1*t) + B2*sin(omega1*t)]

"""

import numpy as np
import matplotlib.pyplot as plt
import math

x0 = 2
v0 = 0
omega = 2*math.pi
omega0 = 5*omega
beta = omega0/20.0
f0 = 1000
t = np.linspace(0, 4, 201)

A = f0/math.sqrt((omega0**2 - omega**2)**2 + 4*beta**2*omega**2)
if omega == omega0:
    delta = math.pi/2
else:
    delta = math.atan(2*beta*omega/(omega0**2 - omega**2))
if delta < 0:
    delta = delta + math.pi
omega1 = math.sqrt(omega0**2 - beta**2)
B1 = x0 - A*math.cos(delta)
B2 = 1.0/omega1*(v0 - omega*A*math.sin(delta) + beta*B1)

print('A = {:2.2f} delta = {:.4f}'.format(A, delta))
print('omega1 = {:1.3f}*pi'.format(omega1/math.pi))
print('B1 = {:2.2f} B2 = {:.4f}'.format(B1, B2))


def xtr(t):
    x = np.exp(-beta*t)*(B1*np.cos(omega1*t) + B2*np.sin(omega1*t))
    return x


def x(t):
    x = A*np.cos(omega*t - delta) + xtr(t)
    return x


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
plt.plot(t, x(t))
plt.plot(t, xtr(t))

plt.show()
