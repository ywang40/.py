# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 20:17:14 2017

@author: Yujia Wang
"""

import numpy as np
import matplotlib.pyplot as plt

l = 1.4e-10 # m, the length of C-C bond
hbar = 1.05457e-34 # J*s
me = 9.109e-31 # kg
NA = 6.022e23 # /mol

def E(n,N):
    return (n**2*np.pi**2*hbar**2/2/me/((N-1)*l)**2*NA/1000) # kJ/mol, return energy of state n in molecule that contains N carbons

N = [2,4,6,8,10] # number of carbons in a molecule
n1,n2,n3,n4,n5,n6 = [],[],[],[],[],[]
for num in N:
    n1.append(E(1,num)) # put energies of n=1 state of the 5 molecules in the list
    n2.append(E(2,num)) # put energies of n=2 state of the 5 molecules in the list
    n3.append(E(3,num)) 
    n4.append(E(4,num))
    n5.append(E(5,num))
    n6.append(E(6,num))
"""create a scatter plot"""
i = 1
for n in [n1,n2,n3,n4,n5,n6]:
    plt.scatter(N,n,label='n={}'.format(i)) # x-axis is the number of carbons in a molecule, y-axis is energy
    i+=1
legend = plt.legend()   
labels = ['Ethylene', 'Butadiene', 'Hexatriene', 'Octatetraene','Decapentaene']
plt.xticks(N, labels, rotation='vertical')
plt.ylabel('Energy(kJ/mol)')
plt.title('The Energies of the n = 1-6 Particle-in-box States')
plt.show()