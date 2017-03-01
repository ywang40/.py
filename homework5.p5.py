#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 17:04:16 2017

@author: ywang40
"""

import numpy as np

l1 = 1.4e-10 # m, the length of ethylene moecule
l2 = 1.4e-10*3 # m, the length of butadiene molecule
hbar = 1.05457e-34 # J*s
me = 9.109e-31 # kg
NA = 6.022e23 # /mol

def E(n,l):
    return (n**2*np.pi**2*hbar**2/2/me/l**2)
E_ethylene = 2*E(1,l1)
E_butadiene = 2*E(1,l2) + 2*E(2,l2)
E_net = E_butadiene - 2*E_ethylene
print(E_ethylene*NA, E_butadiene*NA, E_net*NA)
