#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 11:14:08 2017

@author: ywang40
"""

import numpy as np
import matplotlib.pyplot as plt

l = 1.4*3 # angstrom, the length of the molecule

def Psi_2(x):
      return (2/l)**0.5*np.sin(2*np.pi*x/l) # normalized wavefunction

x = np.linspace(0,l,100)
Psi = Psi_2(x)
p1, = plt.plot(x,Psi,label='$\Psi_2(x)$') # plot the normalized wavefunction
p2, = plt.plot(x,Psi**2,label='$|\Psi_2(x)|^2$') # plot the normalized probability distribution
plt.legend(fontsize = 'small')
plt.xlabel('$x(\AA)$')
plt.ylabel('$\Psi_2(x)(\AA^{-1/2})$, $|\Psi_2(x)|^2(\AA^{-1})$')
plt.title('n = 2 Partical-in-a-box Wavefunction and Probability Distribution',fontsize = 'small')
plt.axhline(y=0,color='k',linestyle='--') # draw a horizontal dash line
plt.annotate('the most probable location', xy=(l/4, Psi_2(l/4)**2), xytext=(1.0, 0.25), arrowprops=dict(facecolor='black', shrink=0.05)) # add annotations
plt.annotate('the most probable location', xy=(3*l/4, Psi_2(3*l/4)**2), xytext=(1.5, 0.65), arrowprops=dict(facecolor='black', shrink=0.05))
plt.annotate('node\naverage location', xy=(l/2, 0), xytext=(1.5, -0.3), arrowprops=dict(facecolor='black', shrink=0.05))
plt.xlim(0,l)
plt.show()

