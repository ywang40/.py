# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 22:12:56 2017

@author: Yujia Wang
"""
import numpy as np
import sympy as sp # import sympy for symbolic mathematics

l = 3*1.4e-10 # m, the length of the box
e = 1.602e-19 # C
def psi(n,x):
    return((2/l)**0.5*sp.sin(n*sp.pi*x/l))

x = sp.symbols('x')
#T,kB,m= symbols('T,kB,m',positive=True)
a = sp.integrate((psi(1,x)*x*psi(3,x)),(x,0,l))
print(a)
b = sp.integrate((psi(2,x)*x*psi(3,x)),(x,0,l))
print(b)