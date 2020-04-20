# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 21:01:39 2019

@author: mrale
Consider a massless wheel of radius R mounted on a frictionless horizontal
axis. A point mass M is glued to the edge, and a massless string is wrapped
several times around the perimeter and hangs vertically down witha mass m
suspended from its bottom end. (See figure 4.28.)Initially I am holding the
wheel with M vertically below the axle. At t=0, I release the wheel, and m
starts to fall vertically down. Solve the equation of motion numerically for
0<=t<=20. Take M=g=R=1 and m=0.7. Plot U(fi) against fi, the angle through the
wheel has turned.
"""
from math import pi, sin
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

M = 1
g = 1
R = 1
m = .8

fi = np.linspace(-pi/4, pi, 201)
U = g*R*(M*(1 - np.cos(fi)) - m*fi)

plt.plot(fi, U)
plt.grid()
plt.show()

t = np.linspace(0, 20, 201)


def dydt(t, y):
    fi, fidot = y
    return (fidot, g/R/(M + m)*(m - M*sin(fi)))


sol = solve_ivp(dydt, [0, 20], [0, 0], t_eval=t)
y = sol.y

plt.plot(t, y[0, :])
plt.show()
