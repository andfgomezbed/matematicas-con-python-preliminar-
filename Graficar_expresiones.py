# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 14:16:59 2020

@author: andfg
"""

from sympy.abc import x, y
from sympy import sympify,solve
from sympy.plotting import plot

expr = input('Enter an expression: ')
var = input('select a variable: ')
expr=sympify(expr)

def graficar_ecu(ecuacion,variable):
    yecu=solve(ecuacion,var)
    yecu=yecu[0]
    plot(yecu)
    
graficar_ecu(expr,var)