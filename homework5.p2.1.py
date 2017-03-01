#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 11:51:59 2017

@author: ywang40
"""

import numpy as np
import matplotlib.pyplot as plt

l = 1.4*3 # angstrom, the length of the molecule

def Psi_2(x):
      return (2/l)**0.5*np.sin(2*np.pi*x/l) # normalized wavefunction

#plt.figure()
x = np.linspace(0,l,100)
Psi_2 = Psi_2(x)
plt.plot(x,Psi_2,label='$\Psi_2(x)')

plt.xlabel('$x(Angstrom)$')
plt.ylabel('$\Psi_2(x)(\AA^{-1/2})$')
plt.annotate('node\naverage location', xy=(l/4, Psi_2(4/l)), xytext=(1.0, -0.3), arrowprops=dict(facecolor='black', shrink=0.05))
#plt.annotate('the most probable location', xy=(l/2, 0), xytext=(1.5, -0.3), arrowprops=dict(facecolor='black', shrink=0.05))
plt.xlim(0,l)
legend=plt.legend()
plt.show()