# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 11:15:49 2020

@author: andfg
"""


# =============================================================================
# multiplicador de expresiones
# =============================================================================

from sympy import expand, sympify, factor, pprint

if __name__=='__main__':
    expr1 = input('Enter the first expression: ')
    expr2 = input('Enter the second expression: ')

def multiplicador_expresiones (u,v):
    expr1=sympify(u)
    expr2=sympify(v)
    
    prod= expand(expr1*expr2)
    result=factor(prod)
    pprint(result)
    
  
multiplicador_expresiones(expr1, expr2)