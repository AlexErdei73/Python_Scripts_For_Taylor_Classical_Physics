# -*- coding: utf-8 -*-
"""
Created on Mon Apr 08 08:44:00 2019

@author: mrale
In Example 7.7 (page 264), we saw that the bead on a spinning hoop can make
small oscillations about its nonzero equilibrium points that are approximately
sinusoidal, with frequency Omega'=(omega**2 - (g/omega/R)**2)**0.5 as in
(7.80).Solve the equation of motion (7.73) numerically and then plot both your
numerical solutulion and the approximate solution on the same graph. Use the
following numbers g=R=1 and omega**2=2, and initial conditions Thetadot(0)=0
and Theta(0)=Thata0 + epsilon0, where epsilon0=1grad.
"""
from math import pi, acos, sqrt, sin, cos
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

g = 1
R = 1
omega = sqrt(2)
eps0 = 1*pi/180
theta0 = acos(g/R/omega**2)
thetadot0 = 0
OMEGA1 = omega*sin(theta0)
t = np.linspace(0, 20, 201)
theta_approx = theta0 + eps0*np.cos(OMEGA1*t)


def dydt(t, y):
    theta, thetadot = y
    return (thetadot,  (omega**2*cos(theta) - g/R)*sin(theta))


sol = solve_ivp(dydt, [0, 20], [theta0 + eps0, thetadot0], t_eval=t)
y = sol.y

plt.plot(t, theta_approx)
plt.plot(t, y[0, :])
plt.show()
