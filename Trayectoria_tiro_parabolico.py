# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 17:05:30 2020

@author: andfg
"""


#### GRAFICANDO CON FORMULAS Y FUNCIONES####

### TRYECTORIA PARABOLICA DE UN PROYECTIL
### incialmente se debe conocer el tiempo de vuelo (2*tiempo hasta la max h)
### con el fin de generar el inervalo de t a uilizar en Sx(t) y Sy(t) funciones
### de posicion en x y y respt.

## generalemte los datos de tiempo son tipo float(dedimales) y la funcion range
## no sirve para crear estos intervalor, por lo que con un ciclo WHILE se resu-
##ve esto.

def frange(start, final, step):
    numbers=[] #lista vacia para meter los valores
    while start < final:
        numbers.append(start)##el arguemnto es para que el inicio se ingrese
        start= start + step
    return numbers

##### crear la trayectoria
import matplotlib.pyplot as plt
import math ###modulo para usar funcines matematicas

#generar la funcion para graficar. se llamara con el num 2
def draw_graph2(x,y):
    plt.plot(x,y)
    plt.xlabel("x-coordinate")
    plt.ylabel("y-coordinate")
    plt.title("projectile motion of a ball")
# generar ka funcion de rangos de tiempodef frange(start, final, step):
def frange(start, final, step):
    numbers=[] #lista vacia para meter los valores
    while start < final:
        numbers.append(start)##el arguemnto es para que el inicio se ingrese
        start= start + step
    return numbers   
##funcion de graficacion completa
def draw_trajectory(u,theta): ## u=V inicial y thetha=angulo en radianes
    theta=math.radians(theta)
    g= 9.8
    #### definir el tiempo de vuelo
    t_flight=2*u*math.sin(theta)/g
    ### definir el intervalo de tiempo
    intervals=frange(0,t_flight,0.001)
    ### crear coordenadas x y y
    x= []
    y= []
    for t in intervals:
        x.append(u*math.cos(theta)*t)
        y.append((u*math.sin(theta)*t - 0.5*g*t*t))
    draw_graph2(x,y)
    
## bloque de interaccion con el usuario
if __name__ == '__main__':
    try:
        u=float(input("ingrese la velocidad inicial (m/s):"))
        theta = float(input('ingrese el angulo de lanzamiento (degrees): '))
    except ValueError:
        print("Usted ingreso una entrada no valida")
    else:
        draw_trajectory(u,theta)
        plt.show() ### si se ejecuta en ventana de comandos
 
###### comparando trayectorias con v diferentes
if __name__ == '__main__':
 # Lista de diferentes velocidades
 u_list = [20, 40, 60]
 theta = 45
 for u in u_list:
     draw_trajectory(u, theta)
# Add a legend and show the graph
 plt.legend(['20', '40', '60'])
 plt.title("trayectorias a v diferentes")
 
 ###### comparando trayectorias con angulos diferentes
if __name__ == '__main__':
 # Lista de diferentes angulos
 theta_list = [20, 45, 60, 90,120]
 u= 25
 for theta in theta_list:
     draw_trajectory(u, theta)
# Add a legend and show the graph
 plt.legend(['20', '45', '60',"90","120"])
 plt.title("trayectorias con angulos diferentes")
 

                 
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    