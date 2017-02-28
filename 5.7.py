# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 19:22:20 2017

@author: Yujia Wang
"""

import numpy as np

l = 1 # m, the length of a side of the box
hbar = 1.05457e-34 # J*s
m = 28.053*1.6605e-27 # kg, the mass of a ethylene molecule
NA = 6.022e23 # /mol

def E(n_square,l):
    return (n_square*np.pi**2*hbar**2/2/m/l**2) # n_square = nx^2+ny^2+nz^2
E_0 = E(3,l) # nx = ny = nz = 1
print(E_0*NA)

k = 1.38065e-23 # J/K
T = 298 # K
KE = 3/2*k*T
n = KE*2*m*l**2/np.pi**2/hbar**2
print(n)

deltaE = E(n+1,l) - E(n,l)
print(deltaE)