# -*- coding: utf-8 -*-
"""
Created on Thu May 23 14:47:49 2019

@author: mrale
Consider a particle with mass m and angular momentum l in the field of a
central force F=-k/r**(5/2).Choose units for which m=l=k=1. Find the value r0
of r at which Ueff is minimum and make a plot of Ueff(r) for 0<r<=5r0.Assuming
now that the particle has energy E=-0.1, find an accurate value of rmin, the
particle's distance of closest approach to the force center. Assuming that the
particle is at r=rmin when fi=0, use a computer program to solve the
transformed radial equation(8.41) and the orbit in the form r=r(fi) for
0<=fi<=7pi. Plot the orbit.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
from scipy.integrate import solve_ivp

m = L = k = 1
r0 = L**4/k**2/m**2
r = np.linspace(1e-6, 5*r0, 201)


def Ueff(r):
    return (-2*k/3.0)*(r**(-1.5)) + (L**2/2.0/m)*(r**(-2.0))


plt.plot(r, Ueff(r))
plt.ylim(-0.25, 0.1)
plt.grid()
plt.title('Effective Potential Energy')
plt.xlabel('r')
plt.ylabel('U')
plt.show()


def f(r, E=-0.1):
    return (Ueff(r) - E)


rmin = fsolve(f, 1e-6)[0]
print 'The minimal distance at -0.1 energy: %5.4f' % rmin
fi = np.linspace(0, 7*np.pi, 501)


def F(u):
    return -k*u**2.5


def dydfi(fi, y):
    u, dudfi = y
    return (dudfi, -u - m/(L**2*u**2)*F(u))


sol = solve_ivp(dydfi, [0, 7*np.pi], [1.0/rmin, 0], t_eval=fi)
y = sol.y
u = y[0, :]
plt.polar(fi, 1.0/u)
plt.title('The orbit')
plt.show()
