# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 11:47:10 2020

@author: andfg
"""


## Como encontrar las raices de una ecuacion cuadrática.##




def roots(a,b,c):
   """
      Para ingresar valores en forma de fraciones es necesario tener el valor
       de a,b o c preexistente en otra variable. Ejm: si el coeficiente a= 2/3
       es nesario crear la variable A=2/3 y utlizarla como arguemto.
       Ejm: roots(A,3,4)

   """
   D = (b*b - 4*a*c)**0.5  #discriminante de la formula cuadratica
   
   X_1 = (-b + D)/(2*a)  #formula cudratica 
   X_2 = (-b - D)/(2*a)
   sol=[X_1, X_2]
   print(sol)
   return sol


if __name__ == '__main__': ## comando para definir entradas para el usuario
    
    a = input('Enter a: ')
    b = input('Enter b: ')
    c = input('Enter c: ')
    roots(float(a), float(b), float(c))
    
    
    
