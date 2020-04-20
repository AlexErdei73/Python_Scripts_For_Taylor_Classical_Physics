# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 12:56:21 2019

@author: mrale
Consider a weakly damped oscillator that is being driven by periodic
rectangular pulses. Let the natural period of the oscillator be tau0=1,
so that the natural frequency is omega0=2*pi, and let the damping constant
be beta=0.1. Let the pulse last for a time deltatau=0.25 and have a height
fmax=1. Calculate the first six Fourier coefficients An for the long-term
motion x(t) of the oscillator, assuming first that the drive period is the
same as the natural period, tau=tau0=1. Plot the resulting motion. Repeat
these exercises for tau=1.5*tau0, 2.0*tau0 and 2.5*tau0.
"""
import math
import numpy as np
import matplotlib.pyplot as plt


def rectpulse(n, tau, fmax=1, deltatau=0.25):
    if n == 0:
        fn = fmax*deltatau/tau
    else:
        fn = 2*fmax/math.pi/n*math.sin(math.pi*n*deltatau/tau)
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


taunumber = [1.0, 1.5, 2.0, 2.5]
nmax = 6
tau0 = 1
beta = 0.1
t = np.linspace(0, 6, 201)
x = np.zeros((len(taunumber), 201))
An = np.zeros((len(taunumber), nmax))
deltan = np.zeros((len(taunumber), nmax))
for k in range(0, len(taunumber)):
    for n in range(0, nmax):
        tau = taunumber[k]*tau0
        An[k, n] = A(n, tau, rectpulse(n, tau), tau0, beta)
        deltan[k, n] = delta(n, tau, tau0, beta)
        x[k] = x[k] + An[k, n]*np.cos(n*2*math.pi/tau*t - deltan[k, n])

for k in range(0, len(taunumber)):
    plt.ylim(-0.4, 0.4)
    plt.ylabel('x(t)')
    plt.xlabel('t')
    plt.title(r'$\tau = ${:4.2f}*$\tau_0$'.format(taunumber[k]))
    plt.grid()
    plt.plot(t, x[k])
    plt.show()

print
s = '                    '
for n in range(0, nmax):
    s = s + ('A{:n}     ').format(n)
print(s)
for k in range(0, len(taunumber)):
    s = 'tau = {:4.2f}*tau0'.format(taunumber[k])
    for n in range(0, nmax):
        s = s + '{:7.0f}'.format(An[k, n]*10000)
    print(s)
