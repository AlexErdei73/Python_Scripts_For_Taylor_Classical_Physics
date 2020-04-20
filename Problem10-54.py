# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 21:23:05 2019
The nutation of a top is controlled by the effective potential energy
Make a plot of it as follows: (a) First, since the second term is constant
you can ignore it. Next, by choice of your units, you can take MgR = 1 =
lambda1. The remaining parameters Lz and L3 are genuinely independent
parameters. To be definite set Lz = 10 and L3 = 8 and plot Ueff(Theta) as a
function of Theta. (b) Explain clearly how you could use your graph to
determine the angle Theta0 at which the top could precesssteadily with
Theta = constant. Find Theta0 to three significant figures. (c) Find the
rate of this steady precession, Omega = dfi/dt, as given by(10.115).
Compare with the approximate value of Omega given by (10.112).
@author: mrale
"""

import matplotlib.pyplot as plt
import numpy as np


def Ueff(Theta, Lz, L3):
    M = g = R = lbda1 = 1
    U = ((Lz - L3*np.cos(Theta))**2/(2*lbda1*(np.sin(Theta))**2) +
         M*g*R*np.cos(Theta))
    return U


Theta = np.linspace(0.4, 1.0, 10000)
Lz = 10
L3 = 8
M = g = R = lbda1 = 1
U = Ueff(Theta, Lz, L3)
plt.plot(Theta, U)
plt.title(r'$U_{eff}(\Theta)$')
plt.show()

imin = np.argmin(U)
print
print('Lz = {:3.1f} L3 = {:3.1f}').format(Lz, L3)
print('Theta0 = {:5.3f}rad').format(Theta[imin])

Omega_approx = L3/(lbda1*np.cos(Theta[imin]))
Omega_exact = (Lz - L3*np.cos(Theta[imin]))/(np.sin(Theta[imin]))**2
print('Omega(approximate) = {:5.3f}').format(Omega_approx)
print('Omega(exact) = {:5.3f}').format(Omega_exact)
