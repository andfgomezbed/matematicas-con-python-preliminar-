# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 16:58:07 2020

@author: andfg
"""





def isfactor(a,b):
    
    
    """
    DETERMINAR SI EL NUMERO b ES FACTOR DE a.
    Parameters
    ----------
    a : NUMERADOR.
    b : DENOMINADOR.

    

      
    """
    if a%b == 0:
        return "si es factor" , "a/b=",  a/b
    
    else:
        return "no es factor", "a/b=", a/b

def factores(a, n = None):
    
    """

  Esta funcion permite encontrar todos los factores positivos de un numero desde 1 hasta
  el argumento n seleccionado. si no se especifica en argumento n se encontraran todos
  los enteros posibles
  
    """
    if n == None:
        n=a
    lista=[]
    for i in range(1,n+1):
        if a % i==0:
            lista.append(i)
    return(lista)


        
        
    



    