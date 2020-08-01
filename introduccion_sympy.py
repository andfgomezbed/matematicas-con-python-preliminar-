# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 09:39:18 2020

@author: andfg
"""
# =============================================================================
# RESUMEN SOBRE SYMPY 
# =============================================================================


# =============================================================================
# 1. Definir simbolos

from sympy import Symbol
x=Symbol("x") #Atribuye a x el valor del simbolo "x"

from sympy import symbols #permite  declarar multiples simbolos en una linea
x,y,z = symbols("x, y, z")

# =============================================================================
# =============================================================================
# 2. Factorizar y expandir expreciones 
from sympy import factor, expand
expr1= x**2 - y**2
factor(expr1) ##factor factoriza un expresion en la medida de lo posible

expr2=(x+2)**3 
expand(expr2) ## expand expande expresiones

# =============================================================================
# =============================================================================
# 3. Modificar orden de impresión
from sympy import pprint ##pprint organiza una exresion en importancia de 
#de léxico 
expr3= 3*x + x**2 - 2  
pprint(expr3)

from sympy import init_printing ##init_pp permite modficar el orden lexico
expr4= x**2 + x*2 - 2
init_printing(order='rev-lex') ##invertir el orden
pprint(expr4)
# =============================================================================
# =============================================================================
# 4. sustituir valores en expresiones con el metodo .subs()
expr5 = x**2 + 4*x*y - y**2
expr5.subs({x:2,y:3}) ##los valores deben ser ingresados como un diccionario
expr5.subs({x:y-1}) # es posible sustituir con expresiones complejas
#5. simplificar expresiones
from sympy import simplify
simplify(expr5) #util cuando se obtienen exrp largas
# =============================================================================
# =============================================================================
# 6. convirtiendo strings en expresiones matematicas
from sympy import sympify ## evita usar Simbol y simbols
expr6= sympify("x**2 + z*4 - d**3")
# =============================================================================
# =============================================================================
# 7. Resolver ecuaciones
from sympy import Symbol ,solve ##solve() resuelve para una incognita de una
                       ## ecuacion que se iguala a 0
x= Symbol("x")
expr7 = 3 + 7 -x
solve(expr7) ### solve() resuleve x para la ecuación 3 + 7 - x = 0
# en caso de tener varios resultados(cuadraticas, sist. Ecuaciones,etc)
#solve devuelve una lista con los posibles valores de la incognita
expr8 = x**2 +  2*x + 4
solve(expr8)
## Si se desea almacenar este resultados en un diccionario (incognita:valor)
# se introduce el argumente dict=True
solve(expr8, dict=True)
# Es posible resolver incognitas en terminos de otros simbolos, es decir,
#elegir para simbolo resolver la ecuacion solve(f,simbolo,...)
from sympy.abc import a,b,c,y
expr9= a*x**2 + b*x + c
solve(expr9,x,dict=True)
# =============================================================================
# =============================================================================
# 8. Resolver Sistemas de Ecuaciones Lineales.
##se usa la funcion solve(), donde el primer argumento es una lista de las
#ecuaciones del sistema que se desa resolver.
expr10 = 2*x + 3*y - 6 # ==  2x + 3y = 6
expr11 = 3*x + 2*y - 12# == 3x + 2y = 12
solve((expr10,expr11),dict=True)
#verifiquemos que si son soluciones
soln=solve((expr10,expr11),dict=True)
soln=soln[0] #sustraemos las soluciones en un diccionarios
expr10.subs({x:soln[x], y:soln[y]}) #sustituimos llamando al valor con su res-
                                    #pectiva clave
# =============================================================================
# =============================================================================
# 9. Graficando con sympy.
from sympy.plotting import plot ##funcio plo()
plot(x**2+2)
plot((x**2 + 2),(x, -5, 5)) ##definir el tamaño del eje x
### brindar titulo y nombres de ejes
plot((x**2+2),(x,-5,5),title="gráfica", xlabel="x", ylabel="x**2 + 2")
# =============================================================================







