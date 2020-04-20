# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 22:59:26 2019

@author: mrale
Calculate the period of the oscillation in
the potential k*x**4, for the case k=m=A=1
with numerical integration
"""

import scipy.integrate as integrate
import math


def U(x):
    k = 1
    return k*x**4


def tau(m, A):
    t = 4*math.sqrt(m/2.0)
    t = t*integrate.quad(lambda x: 1.0/math.sqrt(U(A) - U(x)), 0, A)[0]
    return t


print ('period = %6.3f' % (tau(1, 1)))
