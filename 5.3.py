# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 19:22:20 2017

@author: Yujia Wang
"""

import numpy as np

l = 3*1.4e-10 # m, the length of the box
hbar = 1.05457e-34 # J*s
me = 9.109e-31 # kg
NA = 6.022e23 # /mol
hc = 1240 # ev*nm

def E(n,l):
    return (n**2*np.pi**2*hbar**2/2/me/l**2)*6.2415e18 # eV

E1_3 = E(3,l)-E(1,l) # the energy difference of n=1 and n=3 states
E2_3 = E(3,l)-E(2,l) # the energy difference of n=2 and n=3 states
lamda1_3 = hc/E1_3 # nm
lamda2_3 = hc/E2_3 # nm

print(lamda1_3,lamda2_3)


