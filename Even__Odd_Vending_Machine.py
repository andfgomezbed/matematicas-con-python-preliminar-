# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 12:01:54 2020

@author: andfg
"""


##1: Even-Odd Vending Machine
## este programa permite intricudir un numero y definir si es para o impar
##además arroja una lista con los proximos 9 numeros pares o impares según
##sea el caso

def even_odd(a):
    if a%2 == 0:
        vect=[a]
        cont=a
        for i in range(1,10):
            cont= a + i*2
            vect.append(cont)
        print("el numero es par")
        print(vect)            
    else:
        vect=[a]
        cont=a
        for i in range(1,10):
            cont= a + i*2
            vect.append(cont)
        print("el numero es impar")
        print(vect)

if __name__ == '__main__': ## comando para definir entradas para el usuario
    
    a = input('introdusca un numero: ')
   
    even_odd(float(a))
            
            
            
      
        
        