# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 09:19:19 2019

@author: mrale
Calculate the period of a simple pendulum and
describe it as the function of the amplitude

"""

import numpy as np
import math
import matplotlib.pyplot as plt
import scipy.special as special

fi = np.linspace(0, math.pi, 100)
A = np.sin(fi/2.0)
tau = 2.0/math.pi*special.ellipk(A**2)
plt.plot(fi, tau)
plt.xlabel('Fi(rad)')
plt.ylabel('T/T0')
plt.show()
