# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 12:56:21 2019

@author: mrale
Consider again the oscillator driven by the periodic rectangular pulses. Find
the RMS displacement xrms=sqrt(<x**2>) as given by Parseval's theorem. Using
the same numerical values as before(tau0=1, beta=0.1, fmax=1, deltatau=0.25)
and aproximating the series by its first six terms, make a plot of xrms as a
function of the drive period tau for 0.25<tau<5.5.
"""
import math
import numpy as np
import matplotlib.pyplot as plt


def rectpulse(n, tau, fmax=1, deltatau=0.25):
    if n == 0:
        fn = fmax*deltatau/tau
    else:
        fn = 2*fmax/math.pi/n*np.sin(math.pi*n*deltatau/tau)
    return fn


def A(n, tau, fn, tau0=1, beta=0.1):
    omega0 = 2*math.pi/tau0
    omega = n*2*math.pi/tau
    An = fn*((omega0**2 - omega**2)**2 + 4*beta**2*omega**2)**(-0.5)
    return An


tau = np.linspace(0.25, 5.5, 201)
nmax = 6
for n in range(0, nmax):
    if n == 0:
        xrms = A(n, tau, rectpulse(n, tau))**2
    else:
        xrms = xrms + 0.5*A(n, tau, rectpulse(n, tau))**2
xrms = xrms**0.5

plt.plot(tau, xrms)
titletxt = '''The RMS displacement of a linear oscillator
 driven by periodic rectangular pulses'''
plt.title(titletxt)
plt.xlabel(r'$\tau$')
plt.ylabel(r'$\sqrt{<x^2>}$')
plt.show()
