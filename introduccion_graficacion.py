# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 12:24:00 2020

@author: andfg
"""


##creando gráficas

x=[1,2,3,4,5,6]
y=[1,2,3,4,5,6]

import matplotlib as mpl ## importar el paquete de matplotlib para graficar
from pylab import plot, show ##pylab esta incluido en el paquete
plot(x,y,) ##grafica xvsy, 

plot(x,y, marker="o") #rgt marker permite mostrar los puntos con figuras determinadas
            
plot(x,y,"o") ##la grafica solo genera los puntos pero no los concecta

###ejemplo###
nyc_temp = [53.9, 56.3, 56.4, 53.4, 54.5, 55.8, 56.8, 55.0, 55.3, 54.0, 56.7, 56.4, 57.3]
year=range(2000,2013)
plot(year, nyc_temp, marker="o")

###comparar varias gráficas##
nyc_temp_2000 = [31.3, 37.3, 47.2, 51.0, 63.5, 71.3, 72.3, 72.7, 66.0, 57.0, 45.3, 31.1]
nyc_temp_2006 = [40.9, 35.7, 43.1, 55.7, 63.1, 71.0, 77.9, 75.8, 66.6, 56.2, 51.9, 43.6]
nyc_temp_2012 = [37.3, 40.9, 50.9, 54.8, 65.1, 71.0, 78.8, 76.7, 68.8, 58.0, 43.9, 41.5]
months=range(1,13)
##la funcion plot permite graficas superpuestas, se debe copiar los pares de
## de arguemntos en serie.-
plot(months,nyc_temp_2000,months,nyc_temp_2006,months,nyc_temp_2012)
from pylab import legend #poner leyendas
legend([2000,2002,2016])
from pylab import title, xlabel, ylabel,show #poner titulos y rotulos
title('Average monthly temperature in NYC')
xlabel("Month")
ylabel("Temperature")
####### como  modificar los ejes
nyc_temp = [53.9, 56.3, 56.4, 53.4, 54.5, 55.8, 56.8, 55.0, 55.3, 54.0, 56.7, 56.4, 57.3]
plot(nyc_temp, marker='o')
from pylab import axis
axis() ## esto arroja una lista donde se muestra el rango del eje x y luego el 
            ###rango del eje y
axis(ymin=0) ## hacer que el eje y inicie en 0
## tambien se puede usar xmin,xmax y xmax
##########
## USANDO Pyplot (otro modulo para crear graficas)
import matplotlib.pyplot
def create_graph():  #estamos creando una funcion cuyo utilidad es generar una
    x_numbers= [1,2,3] #una grafica.
    y_numbers=[2,4,6]
    mpl.pyplot.plot(x_numbers, y_numbers)
    mpl.pyplot.show()

create_graph() #se debe llamar la funcion para generar la grafica
### para llamr funciones o identificar atributos en pyplot se usa:
# matplotlib(<como se halla llamado>).pyplot.<funcion/atributo>


