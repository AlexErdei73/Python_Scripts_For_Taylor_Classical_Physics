# -*- coding: utf-8 -*-
"""
Created on Sat Mar 02 21:57:02 2019

@author: mrale
Consider a cart on a spring with natural frequency omega0=2*pi,
which is released from rest at x0=1 and t=0. Plot the position
x(t) for 0<t<2 and for damping constants beta=0,1,2,4,6,2*pi,10
and 20.
"""

import matplotlib.pyplot as plt
import numpy as np

beta = [0, 1, 2, 4, 6, 2*np.pi, 10, 20]
omega0 = 2*np.pi
x0 = 1
t = np.linspace(0, 2, 101)


def x(t, b):
    if b < omega0:
        omega1 = (omega0**2 - b**2)**0.5
        x = x0*np.exp(-b*t)*(np.cos(omega1*t) + b/omega1*np.sin(omega1*t))
    elif b == omega0:
        x = x0*np.exp(-b*t)*(1 + b*t)
    else:
        sr = (b**2 - omega0**2)**0.5
        l1 = b + sr
        l2 = b - sr
        x = x0/2./sr*(l1*np.exp(-l2*t) - l2*np.exp(-l1*t))
    return x


n = len(beta)
for i in range(1, n + 1):
    figure_number = (i - 1)//2 + 1
    subplot_number = (i - 1) % 2 + 1
    if subplot_number == 1:
        plt.figure(figure_number)
        plt.suptitle('Damped Oscillation For Different Dampings')
    plt.subplot(2, 1, subplot_number)
    plt.grid()
    if subplot_number == 1:
        frame1 = plt.gca()
        frame1.axes.xaxis.set_ticklabels([])
    plt.title(r'$\beta$ = {:g}'.format(beta[i - 1]))
    plt.ylabel('x(t)')
    if subplot_number == 2:
        plt.xlabel('t(s)')
    plt.plot(t, x(t, beta[i - 1]))

plt.show()
