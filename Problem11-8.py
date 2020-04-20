# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 17:14:25 2019
The most general motion of the two carts of Section 11.2 is given by (11.21),
with thw constants A1, A2, delta1, and delta2 determined by the initial
conditions. (a) Show that it can be rewritten as [x1(t), x2(t)] =
(B1*cos(omega1*t) + C1*sin(omega1*t))*[1, 1] + (B2*cos(omega2*t) +
C2*sin(omega2*t))*[1, -1]. This form is usually a little more convenient
for matching initial conditions. (b) If the carts are released from rest at
positions x1(0)=x2(0)=A, find the coefficients B1,B2,C1 and C2 and plot x1(t)
and x2(t). Take A=omega1=1 and 0<=t<=30 for your plots. (c)Same as part (b),
except that x1(0)=A but x2(0)=0.
@author: mrale
"""
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

B1, C1, B2, C2, t = sp.symbols('B1 C1 B2 C2 t')
A = omega1 = 1
omega2 = sp.sqrt(3)*omega1
a1_vec = sp.Matrix([1, 1])
a2_vec = sp.Matrix([1, -1])
x_vec = sp.Matrix([0, 0])

x_vec = (B1*sp.cos(omega1*t) + C1*sp.sin(omega1*t))*a1_vec
x_vec += (B2*sp.cos(omega2*t) + C2*sp.sin(omega2*t))*a2_vec
dxdt_vec = sp.diff(x_vec, t)

x0_vec = sp.Matrix([0, 0])
v0_vec = sp.Matrix([0, A])
sol = sp.solve([x_vec.subs(t, 0) - x0_vec, dxdt_vec.subs(t, 0) - v0_vec],
               (B1, B2, C1, C2))
print sol
x_vec_new = x_vec.subs([(B1, sol[B1]), (B2, sol[B2]),
                        (C1, sol[C1]), (C2, sol[C2])])

x_vec_func = sp.lambdify(t, x_vec_new, "numpy")
tval = np.linspace(0, 30, 201)
plt.plot(tval, x_vec_func(tval)[0, 0])
plt.title('Coupled Oscillations')
plt.xlabel('t')
plt.ylabel(r'$x_1$')
plt.show()
plt.plot(tval, x_vec_func(tval)[1, 0])
plt.xlabel('t')
plt.ylabel(r'$x_2$')
plt.show()
