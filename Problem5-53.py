# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 12:56:21 2019

@author: mrale
An oscillator is driven by the periodic force of Problem 5.49, which has period
tau=2. Find the long term motion x(t), assuming the following parameters:
natural period tau0=2 (that is, omega0 = pi), damping parameter beta=0.1, and
maximum drive strength fmax=1. Find the coefficient in the Fourier series for
x(t) and plot the sum of the first four terms in the series for 0<=t<=6.Repeat
, except with natural period equal to 3.
"""
import math
import numpy as np
import matplotlib.pyplot as plt


def triangle(n, tau, fmax=1):
    if n == 0:
        fn = fmax/2.0
    elif n % 2 == 0:
        fn =0
    else:
        fn = 4*fmax/math.pi**2/n**2
    return fn


def A(n, tau, fn, tau0=1, beta=0.2):
    omega0 = 2*math.pi/tau0
    omega = n*2*math.pi/tau
    An = fn*((omega0**2 - omega**2)**2 + 4*beta**2*omega**2)**(-0.5)
    return An


def delta(n, tau, tau0=1, beta=0.2):
    omega0 = 2*math.pi/tau0
    omega = n*2*math.pi/tau
    if omega == omega0:
        delta = math.pi/2
    else:
        delta = math.atan(2*beta*n*omega/(omega0**2 - omega**2))
        if omega0 < omega:
            delta = math.pi + delta
    return delta


tau0 = [2.0, 3.0]
nmax = 6
tau = 2
beta = 0.1
t = np.linspace(0, 6, 201)
x = np.zeros((len(tau0), 201))
An = np.zeros((len(tau0), nmax))
deltan = np.zeros((len(tau0), nmax))
for k in range(0, len(tau0)):
    for n in range(0, nmax):
        An[k, n] = A(n, tau, triangle(n, tau), tau0[k], beta)
        deltan[k, n] = delta(n, tau, tau0[k], beta)
        x[k] = x[k] + An[k, n]*np.cos(n*2*math.pi/tau*t - deltan[k, n])

for k in range(0, len(tau0)):
    plt.ylim(-1, 1)
    plt.ylabel('x(t)')
    plt.xlabel('t')
    plt.title(r'$\tau_0 = ${:4.2f}'.format(tau0[k]))
    plt.grid()
    plt.plot(t, x[k])
    plt.show()

print
s = '                '
for n in range(0, nmax):
    s = s + ('A{:n}     ').format(n)
print(s)
for k in range(0, len(tau0)):
    s = 'tau0 = {:4.2f}'.format(tau0[k])
    for n in range(0, nmax):
        s = s + '{:7.0f}'.format(An[k, n]*10000)
    print(s)
