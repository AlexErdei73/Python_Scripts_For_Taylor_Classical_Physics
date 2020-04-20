# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 15:47:21 2019

@author: mrale
An aircraft whose airspeed is v0 has to fly from town O (at the origin) to
town P, which is a distance D due east. There is a steady gentle wind sheer,
such that vwind=Vy to the y direction, where x and y are measured east and
north respectively. It can be shown, that y(x)=lambda*x*(D - x) is the equation
of the path, which solution of the Euler-Lagrange equation, if 
lambda = (sqrt(4 + 2*k**2*D**2) - 2)/(k*D**2) and y' and fi(the angle by which 
the plane heads to the north of east) both remain small). How much time does 
the plane save by following this path? D=2000mi, v0=500mph and V=0.5mph/mi.
"""
import scipy.integrate as integrate

v0 = 500  #parameters of the problem
D = 2000
V = 0.5
k = V/v0
lam = ((4 + 2*k**2*D**2)**0.5 - 2)/(k*D**2) #the lambda parameter of
                                            #the minimal path


def y(x): #the function of the path
    return lam*x*(D - x)


def dydx(x): #the derivative function
    return lam*D - 2*lam*x


def f(x): #the integrand
    return (1 + dydx(x)**2)**0.5/(1 + k*y(x))


i = integrate.quad(f, 0, D) #numerical integration to calculate the flytime

t0 = round(i[0] / v0, 3) #flytime in hours with 3 decimal precision
print 'The flytime={:g}h'.format(t0)
t = D/v0 - t0  #saved time
print 'The saved time ={:3.1f}min'.format(60*t) #printing it in minutes
