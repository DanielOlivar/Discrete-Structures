"""
#Funciones lineales

from matplotlib import pyplot

#Ejemplo 1: Tenemos la función f(x)=3x+2, donde m=3 y b=2

def f1(x):
    return 3*x + 2

x = range(-5,5)
pyplot.plot(x,[f1(i) for i in x])
pyplot.axhline(0, color = "black")
pyplot.axvline(0, color = "black")
pyplot.title("Ejemplo Función Lineal f(x)=3x+2",fontsize = 18, color = "green")
pyplot.xlabel("Eje x")
pyplot.ylabel("Eje y")
pyplot.grid(color = "gray",linestyle = 'dashed')
pyplot.show()

"""



"""
#Funcipon definida por partes
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2,6)
y = np.piecewise(x,[(x<=0)&(x>=-2),(x<=1)&(x>=0),(x<=3)&(x>=1),(x<=5)&(x>=3)],[-2, lambda x: x+2,lambda x:0.5*x-1.5,lambda x:-0.5*x+2.5])

plt.plot(x,y)
plt.grid()
plt.show()

"""


"""
#Funciones polinomiales
from matplotlib import pyplot
#Ejemplo: Tenemos la función f(x)=x^3-3x^2-x+4

def f1(x):
    return x**3 - 3*x**2 - x + 4

x = range(-7,7)
pyplot.plot(x,[f1(i) for i in x])
pyplot.axhline(0, color = "black")
pyplot.axvline(0, color = "black")
pyplot.ylim(-7, 7)
pyplot.title("Ejemplo Función Polinomial f(x)=x^3-3x^2-x+4",fontsize = 18, color = "green")
pyplot.xlabel("Eje x")
pyplot.ylabel("Eje y")
pyplot.grid(color = "gray",linestyle = 'dashed')
pyplot.show()

"""





"""
#Función Potencia
from matplotlib import pyplot
def f_lineal(x):
    return 2*x**2
x = range(-50,50)
pyplot.plot(x,[f_lineal(i) for i in x])
pyplot.title("Intervalo [-50, 50]",fontsize=10, color="black")
pyplot.axhline(0,color="red")
pyplot.axvline(0,color="red")
pyplot.xlabel("Eje x")
pyplot.ylabel("Eje y")
pyplot.grid(color="gray",linestyle="dashed")
pyplot.show()

"""




"""
#Funciones racionales

import numpy as np
from matplotlib import pyplot

def f_racional(x):
    return 1/x
x = range(1,50)
pyplot.plot(x,[f_racional(i) for i in x])
pyplot.title("Intervalo [1, 50]",fontsize=10, color="black")
pyplot.axhline(0,color="red")
pyplot.axvline(0,color="red")
pyplot.xlabel("Eje x")
pyplot.ylabel("Eje y")
pyplot.grid(color="gray",linestyle="dashed")
pyplot.show()

"""



"""
#Funciones algebraicas
from matplotlib import pyplot
import math

def funcion1(x):
    return x**2+5*x
def funcion2(x):
    return 5*x+4

x= range(-10,10)

pyplot.plot(x,[funcion1(i) for i in x],color='orange')
pyplot.axhline(0, color = "brown")
pyplot.axvline(0, color = "brown")
pyplot.title("Función algebraica f(x)=x**2+5*x",fontsize = 20, color = "brown")
pyplot.xlabel("Eje x")
pyplot.ylabel("Eje y")
pyplot.grid(color = "gray",linestyle = 'dashed')
pyplot.show()

pyplot.plot(x,[funcion2(i) for i in x],color='orange')
pyplot.axhline(0, color = "brown")
pyplot.axvline(0, color = "brown")
pyplot.title("Función algebraica f(x)=5*x+4",fontsize = 20, color = "brown")
pyplot.xlabel("Eje x")
pyplot.ylabel("Eje y")
pyplot.grid(color = "gray",linestyle = 'dashed')
pyplot.show()

"""



"""
#Funciones trigonométricas

from matplotlib import pyplot
import math
import numpy as np

def funcion1(x):
    return math.sin(x)
def funcion2(x):
    return math.cos(x)
x = np.arange (-10,10,0.1)

pyplot.plot(x,[funcion1(i) for i in x],color='orange')
pyplot.axhline(0, color = "brown")
pyplot.axvline(0, color = "brown")
pyplot.title("Función trigonometrica f(x)= senx ",fontsize = 20, color = "brown")
pyplot.xlabel("Eje x")
pyplot.ylabel("Eje y")
pyplot.grid(color = "gray",linestyle = 'dashed')
pyplot.show()

pyplot.plot(x,[funcion2(i) for i in x],color='orange')
pyplot.axhline(0, color = "brown")
pyplot.axvline(0, color = "brown")
pyplot.title("Función trigonometrica g(x)=cosx",fontsize = 20, color = "brown")
pyplot.xlabel("Eje x")
pyplot.ylabel("Eje y")
pyplot.grid(color = "gray",linestyle = 'dashed')
pyplot.show()

"""


"""
#Funciones exponenciales
from matplotlib import pyplot
import math

#Definición de funciones

def funcion1(x):
    return 2**x
def funcion2(x):
    return (1/2)**x
x= range(-10,10)
pyplot.plot(x,[funcion1(i) for i in x],color='orange')
pyplot.axhline(0, color = "brown")
pyplot.axvline(0, color = "brown")
pyplot.title("Función exponencial f(x)= 2^(x) ",fontsize = 20, color = "brown")
pyplot.xlabel("Eje x")
pyplot.ylabel("Eje y")
pyplot.grid(color = "gray",linestyle = 'dashed')
pyplot.show()

pyplot.plot(x,[funcion2(i) for i in x],color='orange')
pyplot.axhline(0, color = "brown")
pyplot.axvline(0, color = "brown")
pyplot.title("Función exponencial g(x)=((1)/(2))^(x)",fontsize = 20, color = "brown")
pyplot.xlabel("Eje x")
pyplot.ylabel("Eje y")
pyplot.grid(color = "gray",linestyle = 'dashed')
pyplot.show()
"""




"""
#Función Logarítmica
#Sea la función f(x)=log(2x-4, 2)

import math
from matplotlib import pyplot

def f1(x):
    return math.log(2*x-4, 2)

x = range (3,100)
pyplot.plot(x,[f1(i) for i in x],'b')
pyplot.axhline(0, color = 'violet')
pyplot.axvline(0, color = 'violet')
pyplot.title("Funcion Logarítmica \nIntervalo [3,100]", fontsize=14,color='purple')
pyplot.xlabel("Eje x")
pyplot.ylabel("Eje y")
pyplot.grid(color= "gray",linestyle = 'dashed')
pyplot.show()
"""


"""
#Funciones constantes

import numpy as np
import matplotlib.pyplot as plt

def f_constante(x):
    return 3
x = range(1,50)
pyplot.plot(x,[f_constante(i) for i in x])
pyplot.title("Intervalo [1, 50]",fontsize=10, color="black")
pyplot.axhline(0,color="red")
pyplot.axvline(0,color="red")
pyplot.xlabel("Eje x")
pyplot.ylabel("Eje y")
pyplot.grid(color="gray",linestyle="dashed")
pyplot.show()

"""





"""
#Función Valor absoluto
#Sea la función f(x)=1+|2x+4|


def f2(x):
    return 1+abs(2*x+4) 

x = range (-10,10)
pyplot.plot(x,[f2(i) for i in x],'b')
pyplot.axhline(0, color = 'violet')
pyplot.axvline(0, color = 'violet')
pyplot.title("Funcion Valor Absoluto \nIntervalo [-10,10]", fontsize=14,color='purple')
pyplot.xlabel("Eje x")
pyplot.ylabel("Eje y")
pyplot.grid(color= "gray",linestyle = 'dashed')
pyplot.show()
"""





"""

#Operaciones con funciones

#Función Polinomial
#Gráfica f(x)

from matplotlib import pyplot
def f1(x):
    return ((x**2)-12)/(x-1)
x = range(-10,1)
pyplot.plot(x,[f1(i) for i in x])
pyplot.title("Suma de funciones racionales, intervalo [-10, 1]",fontsize=10, color="black")
pyplot.axhline(0,color="red")
pyplot.axvline(0,color="red")
pyplot.xlabel("Eje x")
pyplot.ylabel("Eje y")
pyplot.grid(color="gray",linestyle="dashed")
pyplot.show()

#Gráfica g(x)

from matplotlib import pyplot
def f1(x):
    return (x-3)/(x-2)
x = range(-10,1)
pyplot.plot(x,[f1(i) for i in x])
pyplot.title("Suma de funciones racionales, intervalo [-10, 1]",fontsize=10, color="black")
pyplot.axhline(0,color="red")
pyplot.axvline(0,color="red")
pyplot.xlabel("Eje x")
pyplot.ylabel("Eje y")
pyplot.grid(color="gray",linestyle="dashed")
pyplot.show()


#Suma
#Intervalo [-10,1]

from matplotlib import pyplot
def f1(x):
    return ((x**3)-(x**2)-16*x+27)/((x**2)-3*x+2)
x = range(-10,1)
pyplot.plot(x,[f1(i) for i in x])
pyplot.title("Suma de funciones racionales, intervalo [-10, 1]",fontsize=10, color="black")
pyplot.axhline(0,color="red")
pyplot.axvline(0,color="red")
pyplot.xlabel("Eje x")
pyplot.ylabel("Eje y")
pyplot.grid(color="gray",linestyle="dashed")
pyplot.show()


#Intervalo [3,15]

from matplotlib import pyplot
def f1(x):
    return ((x**3)-(x**2)-16*x+27)/((x**2)-3*x+2)
x = range(3,15)
pyplot.plot(x,[f1(i) for i in x])
pyplot.title("Suma de funciones racionales, intervalo [3, 15]",fontsize=10, color="black")
pyplot.axhline(0,color="red")
pyplot.axvline(0,color="red")
pyplot.xlabel("Eje x")
pyplot.ylabel("Eje y")
pyplot.grid(color="gray",linestyle="dashed")
pyplot.show()

#Resta
#Intervalo [-10,1]

from matplotlib import pyplot
def f1(x):
    return ((x**3)-3*(x**2)-8*x+21)/((x**2)-3*x+2)
x = range(-10,1)
pyplot.plot(x,[f1(i) for i in x])
pyplot.title("Resta de funciones racionales, intervalo [-10, 1]",fontsize=10, color="black")
pyplot.axhline(0,color="red")
pyplot.axvline(0,color="red")
pyplot.xlabel("Eje x")
pyplot.ylabel("Eje y")
pyplot.grid(color="gray",linestyle="dashed")
pyplot.show()

#Intervalo [3,10]

from matplotlib import pyplot
def f1(x):
    return ((x**3)-3*(x**2)-8*x+21)/((x**2)-3*x+2)
x = range(3,10)
pyplot.plot(x,[f1(i) for i in x])
pyplot.title("Resta de funciones racionales, intervalo [3, 10]",fontsize=10, color="black")
pyplot.axhline(0,color="red")
pyplot.axvline(0,color="red")
pyplot.xlabel("Eje x")
pyplot.ylabel("Eje y")
pyplot.grid(color="gray",linestyle="dashed")
pyplot.show()


#Multiplicación
#Intervalo [-10,1]

from matplotlib import pyplot
def f1(x):
    return ((x**3)-3*(x**2)-12*x+36)/((x**2)-3*x+2)
x = range(-10,1)
pyplot.plot(x,[f1(i) for i in x])
pyplot.title("Multiplicación de funciones racionales, intervalo [-10, 1]",fontsize=10, color="black")
pyplot.axhline(0,color="red")
pyplot.axvline(0,color="red")
pyplot.xlabel("Eje x")
pyplot.ylabel("Eje y")
pyplot.grid(color="gray",linestyle="dashed")
pyplot.show()

#Intervalo[3.10]

from matplotlib import pyplot
def f1(x):
    return ((x**3)-3*(x**2)-12*x+36)/((x**2)-3*x+2)
x = range(3,10)
pyplot.plot(x,[f1(i) for i in x])
pyplot.title("Multiplicación de funciones racionales, intervalo [3, 10]",fontsize=10, color="black")
pyplot.axhline(0,color="red")
pyplot.axvline(0,color="red")
pyplot.xlabel("Eje x")
pyplot.ylabel("Eje y")
pyplot.grid(color="gray",linestyle="dashed")
pyplot.show()



#División
#Intervalo [-10,1]

from matplotlib import pyplot
def f1(x):
    return ((x**3)-2*(x**2)-12*x+24)/((x**2)-4*x+3)
x = range(-10,1)
pyplot.plot(x,[f1(i) for i in x])
pyplot.title("División de funciones racionales, intervalo [-10, 1]",fontsize=10, color="black")
pyplot.axhline(0,color="red")
pyplot.axvline(0,color="red")
pyplot.xlabel("Eje x")
pyplot.ylabel("Eje y")
pyplot.grid(color="gray",linestyle="dashed")
pyplot.show()

#Intervalo[4,15]

from matplotlib import pyplot
def f1(x):
    return ((x**3)-2*(x**2)-12*x+24)/((x**2)-4*x+3)
x = range(4,15)
pyplot.plot(x,[f1(i) for i in x])
pyplot.title("División de funciones racionales, intervalo [4, 15]",fontsize=10, color="black")
pyplot.axhline(0,color="red")
pyplot.axvline(0,color="red")
pyplot.xlabel("Eje x")
pyplot.ylabel("Eje y")
pyplot.grid(color="gray",linestyle="dashed")
pyplot.show()



#Composición (fog)(x)
#Intervalo [-10,2]

from matplotlib import pyplot
def f1(x):
    return (-11*(x**2)+42*x-39)/(x-2)
x = range(-10,2)
pyplot.plot(x,[f1(i) for i in x])
pyplot.title("Composición de funciones racionales, intervalo [-10, 2]",fontsize=10, color="black")
pyplot.axhline(0,color="red")
pyplot.axvline(0,color="red")
pyplot.xlabel("Eje x")
pyplot.ylabel("Eje y")
pyplot.grid(color="gray",linestyle="dashed")
pyplot.show()

#Intervalo[3,15]

from matplotlib import pyplot
def f1(x):
    return (-11*(x**2)+42*x-39)/(x-2)
x = range(3,15)
pyplot.plot(x,[f1(i) for i in x])
pyplot.title("Composición de funciones racionales, intervalo [3, 15]",fontsize=10, color="black")
pyplot.axhline(0,color="red")
pyplot.axvline(0,color="red")
pyplot.xlabel("Eje x")
pyplot.ylabel("Eje y")
pyplot.grid(color="gray",linestyle="dashed")
pyplot.show()

#Composición (gof)(x)
#Intervalo [-20,20]

from matplotlib import pyplot
def f1(x):
    return ((x**2)-3*x-9)/((x**2)-2*x-10)
x = range(-20,20)
pyplot.plot(x,[f1(i) for i in x])
pyplot.title("Composición de funciones racionales, intervalo [-20, 20]",fontsize=10, color="black")
pyplot.axhline(0,color="red")
pyplot.axvline(0,color="red")
pyplot.xlabel("Eje x")
pyplot.ylabel("Eje y")
pyplot.grid(color="gray",linestyle="dashed")
pyplot.show()


#Función Lineal
#Suma

def f1(x):
    return 2*x + 1

def f2(x):
    return 5*x - 3

def f3(x):
    return (2*x + 1) + (5*x - 3)

x = range(-4,4)
pyplot.plot(x,[f1(i) for i in x])
pyplot.axhline(0, color = "black")
pyplot.axvline(0, color = "black")
pyplot.title("Función Lineal f1(x)=2x+1",fontsize = 18, color = "brown")
pyplot.xlabel("Eje x")
pyplot.ylabel("Eje y")
pyplot.grid(color = "gray",linestyle = 'dashed')
pyplot.show()

pyplot.plot(x,[f2(i) for i in x])
pyplot.axhline(0, color = "black")
pyplot.axvline(0, color = "black")
pyplot.title("Función Lineal f2(x)=5x-3",fontsize = 18, color = "magenta")
pyplot.xlabel("Eje x")
pyplot.ylabel("Eje y")
pyplot.grid(color = "gray",linestyle = 'dashed')
pyplot.show()

pyplot.plot(x,[f3(i) for i in x])
pyplot.axhline(0, color = "black")
pyplot.axvline(0, color = "black")
pyplot.title("Función Lineal f3(x)=7x-2",fontsize = 18, color = "purple")
pyplot.xlabel("Eje x")
pyplot.ylabel("Eje y")
pyplot.grid(color = "gray",linestyle = 'dashed')
pyplot.show()

#Resta

def f1(x):
    return 9*x - 5

def f2(x):
    return 4*x + 1

def f3(x):
    return (9*x -5) - (4*x + 1)

x = range(-4,4)
pyplot.plot(x,[f1(i) for i in x])
pyplot.axhline(0, color = "black")
pyplot.axvline(0, color = "black")
pyplot.title("Función Lineal f1(x)=9x-5",fontsize = 18, color = "orange")
pyplot.xlabel("Eje x")
pyplot.ylabel("Eje y")
pyplot.grid(color = "gray",linestyle = 'dashed')
pyplot.show()

pyplot.plot(x,[f2(i) for i in x])
pyplot.axhline(0, color = "black")
pyplot.axvline(0, color = "black")
pyplot.title("Función Lineal f2(x)=4x+1",fontsize = 18, color = "green")
pyplot.xlabel("Eje x")
pyplot.ylabel("Eje y")
pyplot.grid(color = "gray",linestyle = 'dashed')
pyplot.show()

pyplot.plot(x,[f3(i) for i in x])
pyplot.axhline(0, color = "black")
pyplot.axvline(0, color = "black")
pyplot.title("Función Lineal f3(x)=5x-6",fontsize = 18, color = "red")
pyplot.xlabel("Eje x")
pyplot.ylabel("Eje y")
pyplot.grid(color = "gray",linestyle = 'dashed')
pyplot.show()


#Multiplicacion

def f1(x):
    return x + 3

def f2(x):
    return x + 1

def f3(x):
    return (x + 3) * (x + 1)

x = range(-7,7)
pyplot.plot(x,[f1(i) for i in x])
pyplot.axhline(0, color = "black")
pyplot.axvline(0, color = "black")
pyplot.title("Función Lineal f1(x)=x+3",fontsize = 18, color = "purple")
pyplot.xlabel("Eje x")
pyplot.ylabel("Eje y")
pyplot.grid(color = "gray",linestyle = 'dashed')
pyplot.show()

pyplot.plot(x,[f2(i) for i in x])
pyplot.axhline(0, color = "black")
pyplot.axvline(0, color = "black")
pyplot.title("Función Lineal f2(x)=x+1",fontsize = 18, color = "pink")
pyplot.xlabel("Eje x")
pyplot.ylabel("Eje y")
pyplot.grid(color = "gray",linestyle = 'dashed')
pyplot.show()

pyplot.plot(x,[f3(i) for i in x])
pyplot.axhline(0, color = "black")
pyplot.axvline(0, color = "black")
pyplot.title("Función cuadrática f3(x)=x^2+4x+3",fontsize = 18, color = "blue")
pyplot.xlabel("Eje x")
pyplot.ylabel("Eje y")
pyplot.grid(color = "gray",linestyle = 'dashed')
pyplot.show()

#Division

def f1(x):
    return x - 3

def f2(x):
    return x - 1

def f3(x):
    return (x - 3) / (x - 1)

x = range(-7,7)
pyplot.plot(x,[f1(i) for i in x])
pyplot.axhline(0, color = "black")
pyplot.axvline(0, color = "black")
pyplot.title("Función Lineal f1(x)=x-3",fontsize = 18, color = "magenta")
pyplot.xlabel("Eje x")
pyplot.ylabel("Eje y")
pyplot.grid(color = "gray",linestyle = 'dashed')
pyplot.show()

pyplot.plot(x,[f2(i) for i in x])
pyplot.axhline(0, color = "black")
pyplot.axvline(0, color = "black")
pyplot.title("Función Lineal f2(x)=x-1",fontsize = 18, color = "brown")
pyplot.xlabel("Eje x")
pyplot.ylabel("Eje y")
pyplot.grid(color = "gray",linestyle = 'dashed')
pyplot.show()

x1 = range(-15,1)
pyplot.plot(x1,[f3(i) for i in x1])
pyplot.axhline(0, color = "black")
pyplot.axvline(0, color = "black")
pyplot.title("Función Lineal f3(x)=x-3/x-1",fontsize = 18, color = "orange")
pyplot.ylim(0, 8)
pyplot.xlabel("Eje x")
pyplot.ylabel("Eje y")
pyplot.grid(color = "gray",linestyle = 'dashed')
pyplot.show()
x2 =range(2,15)
pyplot.plot(x2,[f3(i) for i in x2])
pyplot.axhline(0, color = "black")
pyplot.axvline(0, color = "black")
pyplot.title("Función Lineal f3(x)=x-3/x-1",fontsize = 18, color = "orange")
pyplot.ylim(-7, 2)
pyplot.xlabel("Eje x")
pyplot.ylabel("Eje y")
pyplot.grid(color = "gray",linestyle = 'dashed')
pyplot.show()


#Composición de funciones

def f1(x):
    return 3*x + 4

def f2(x):
    return 2*x + 1

def fog(x):
    return 3*(2*x+1)+ 4

def gof(x):
    return 2*(3*x+4)+1

x = range(-5,5)
pyplot.plot(x,[f1(i) for i in x])
pyplot.axhline(0, color = "black")
pyplot.axvline(0, color = "black")
pyplot.title("Función Lineal f1(x)=3x+4",fontsize = 18, color = "orange")
pyplot.xlabel("Eje x")
pyplot.ylabel("Eje y")
pyplot.grid(color = "gray",linestyle = 'dashed')
pyplot.show()

pyplot.plot(x,[f2(i) for i in x])
pyplot.axhline(0, color = "black")
pyplot.axvline(0, color = "black")
pyplot.title("Función Lineal g(x)=2x+1",fontsize = 18, color = "blue")
pyplot.xlabel("Eje x")
pyplot.ylabel("Eje y")
pyplot.grid(color = "gray",linestyle = 'dashed')
pyplot.show()

pyplot.plot(x,[fog(i) for i in x])
pyplot.axhline(0, color = "black")
pyplot.axvline(0, color = "black")
pyplot.title("Función lineal fog(x)=6x+7",fontsize = 18, color = "red")
pyplot.xlabel("Eje x")
pyplot.ylabel("Eje y")
pyplot.grid(color = "gray",linestyle = 'dashed')
pyplot.show()

pyplot.plot(x,[gof(i) for i in x])
pyplot.axhline(0, color = "black")
pyplot.axvline(0, color = "black")
pyplot.title("Función lineal gof(x)=6x+9",fontsize = 18, color = "red")
pyplot.xlabel("Eje x")
pyplot.ylabel("Eje y")
pyplot.grid(color = "gray",linestyle = 'dashed')
pyplot.show()


#Operaciones con Funciones Polinomiales
#Ejemplo de la Suma

def f1(x):
    return 5*x**2 + 2*x - 1

def f2(x):
    return -2*x**2 + x + 3

def f3(x):
    return (5*x**2 + 2*x - 1) + (-2*x**2 + x + 3)

x = range(-4,4)
pyplot.plot(x,[f1(i) for i in x])
pyplot.axhline(0, color = "black")
pyplot.axvline(0, color = "black")
pyplot.title("Función Polinomial f1(x)=5x^2+2x-1",fontsize = 18, color = "brown")
pyplot.xlabel("Eje x")
pyplot.ylabel("Eje y")
pyplot.grid(color = "gray",linestyle = 'dashed')
pyplot.show()

pyplot.plot(x,[f2(i) for i in x])
pyplot.axhline(0, color = "black")
pyplot.axvline(0, color = "black")
pyplot.title("Función Polinomial f2(x)=-2x^2+x+3",fontsize = 18, color = "magenta")
pyplot.xlabel("Eje x")
pyplot.ylabel("Eje y")
pyplot.grid(color = "gray",linestyle = 'dashed')
pyplot.show()

pyplot.plot(x,[f3(i) for i in x])
pyplot.axhline(0, color = "black")
pyplot.axvline(0, color = "black")
pyplot.title("Función Polinomial f3(x)=3x^2+3x+2",fontsize = 18, color = "purple")
pyplot.xlabel("Eje x")
pyplot.ylabel("Eje y")
pyplot.grid(color = "gray",linestyle = 'dashed')
pyplot.show()

#Ejemplo de la resta

def f1(x):
    return 2*x**3 - x**2 + 4*x - 2

def f2(x):
    return x**3 - 3*x + 5

def f3(x):
    return (2*x**3 - x**2 + 4*x - 2) - (x**3 - 3*x + 5)

x = range(-6,6)
pyplot.plot(x,[f1(i) for i in x])
pyplot.axhline(0, color = "black")
pyplot.axvline(0, color = "black")
pyplot.title("Función Polinomial f1(x)=2x^3-x^2+4x-2",fontsize = 18, color = "orange")
pyplot.ylim(-50, 50)
pyplot.xlabel("Eje x")
pyplot.ylabel("Eje y")
pyplot.grid(color = "gray",linestyle = 'dashed')
pyplot.show()

pyplot.plot(x,[f2(i) for i in x])
pyplot.axhline(0, color = "black")
pyplot.axvline(0, color = "black")
pyplot.title("Función Polinomial f2(x)=x^3-3x+5",fontsize = 18, color = "green")
pyplot.ylim(-30, 30)
pyplot.xlabel("Eje x")
pyplot.ylabel("Eje y")
pyplot.grid(color = "gray",linestyle = 'dashed')
pyplot.show()

pyplot.plot(x,[f3(i) for i in x])
pyplot.axhline(0, color = "black")
pyplot.axvline(0, color = "black")
pyplot.title("Función Polinomial f3(x)=x^3-x^2+7x-7",fontsize = 18, color = "red")
pyplot.ylim(-50, 50)
pyplot.xlabel("Eje x")
pyplot.ylabel("Eje y")
pyplot.grid(color = "gray",linestyle = 'dashed')
pyplot.show()

#Ejemplo de la multiplicacion

def f1(x):
    return 2*x**2 - 3

def f2(x):
    return 2*x**3 -3*x**2 + 4*x + 5

def f3(x):
    return (2*x**2 - 3) * (2*x**3 -3*x**2 + 4*x + 5)

x = range(-7,7)
pyplot.plot(x,[f1(i) for i in x])
pyplot.axhline(0, color = "black")
pyplot.axvline(0, color = "black")
pyplot.title("Función Polinomial f1(x)=2x^2 − 3",fontsize = 18, color = "purple")
pyplot.xlabel("Eje x")
pyplot.ylabel("Eje y")
pyplot.grid(color = "gray",linestyle = 'dashed')
pyplot.show()

pyplot.plot(x,[f2(i) for i in x])
pyplot.axhline(0, color = "black")
pyplot.axvline(0, color = "black")
pyplot.title("Función Polinomial f2(x)=2x^3 − 3x^2 + 4x + 5",fontsize = 18, color = "pink")
pyplot.ylim(-50, 50)
pyplot.xlabel("Eje x")
pyplot.ylabel("Eje y")
pyplot.grid(color = "gray",linestyle = 'dashed')
pyplot.show()

pyplot.plot(x,[f3(i) for i in x])
pyplot.axhline(0, color = "black")
pyplot.axvline(0, color = "black")
pyplot.title("Función Polinomial f3(x)=4x^5-6x^4+2x^3+19x^2-12x-15",fontsize = 15, color = "blue")
pyplot.ylim(-80, 80)
pyplot.xlabel("Eje x")
pyplot.ylabel("Eje y")
pyplot.grid(color = "gray",linestyle = 'dashed')
pyplot.show()

#Ejemplo de la division

def f1(x):
    return 3*x**3 - 4*x**2 - 5*x + 2

def f2(x):
    return x - 2

def f3(x):
    return 3*x**2 + 2*x -1 

x = range(-7,7)
pyplot.plot(x,[f1(i) for i in x])
pyplot.axhline(0, color = "black")
pyplot.axvline(0, color = "black")
pyplot.title("Función Polinomial f1(x)=3x^3-4x^2-5x+2",fontsize = 18, color = "magenta")
pyplot.ylim(-25, 25)
pyplot.xlabel("Eje x")
pyplot.ylabel("Eje y")
pyplot.grid(color = "gray",linestyle = 'dashed')
pyplot.show()

pyplot.plot(x,[f2(i) for i in x])
pyplot.axhline(0, color = "black")
pyplot.axvline(0, color = "black")
pyplot.title("Función Polinomial f2(x)=x-2",fontsize = 18, color = "brown")
pyplot.xlabel("Eje x")
pyplot.ylabel("Eje y")
pyplot.grid(color = "gray",linestyle = 'dashed')
pyplot.show()

pyplot.plot(x,[f3(i) for i in x])
pyplot.axhline(0, color = "black")
pyplot.axvline(0, color = "black")
pyplot.title("Función Polinomial f3(x)=3x^2+2x-1",fontsize = 18, color = "red")
pyplot.ylim(-5, 50)
pyplot.xlabel("Eje x")
pyplot.ylabel("Eje y")
pyplot.grid(color = "gray",linestyle = 'dashed')
pyplot.show()

#Ejemplo de la composicion de funciones

def f1(x):
    return x**2 - 1

def f2(x):
    return x**3 - 3*x**2 -2*x + 3  

def fog(x):
    return (x**3 - 3*x**2 -2*x + 3)**2 - 1

def gof(x):
    return (x**2 - 1)**3 - 3*(x**2 - 1)**2 -2*(x**2 - 1) + 3 

x = range(-7,7)
pyplot.plot(x,[f1(i) for i in x])
pyplot.axhline(0, color = "black")
pyplot.axvline(0, color = "black")
pyplot.title("Función Polinomial f(x)=x^2-1",fontsize = 18, color = "orange")
pyplot.xlabel("Eje x")
pyplot.ylabel("Eje y")
pyplot.grid(color = "gray",linestyle = 'dashed')
pyplot.show()

pyplot.plot(x,[f2(i) for i in x])
pyplot.axhline(0, color = "black")
pyplot.axvline(0, color = "black")
pyplot.title("Función Polinomial g(x)=x^3-3x^2-2x+3",fontsize = 18, color = "blue")
pyplot.ylim(-20, 20)
pyplot.xlabel("Eje x")
pyplot.ylabel("Eje y")
pyplot.grid(color = "gray",linestyle = 'dashed')
pyplot.show()

pyplot.plot(x,[fog(i) for i in x])
pyplot.axhline(0, color = "black")
pyplot.axvline(0, color = "black")
pyplot.title("Función Polinomial fog(x)=x^6-6x^5+5x^4+18x^3-14x^2-12x+8",fontsize = 10, color = "red")
pyplot.xlim(-5, 5)
pyplot.ylim(-5, 30)
pyplot.xlabel("Eje x")
pyplot.ylabel("Eje y")
pyplot.grid(color = "gray",linestyle = 'dashed')
pyplot.show()

pyplot.plot(x,[gof(i) for i in x])
pyplot.axhline(0, color = "black")
pyplot.axvline(0, color = "black")
pyplot.title("Función polinomial gof(x)=x^6-6x^4+7x^2+1",fontsize = 10, color = "red")
pyplot.ylim(-10, 30)
pyplot.xlabel("Eje x")
pyplot.ylabel("Eje y")
pyplot.grid(color = "gray",linestyle = 'dashed')
pyplot.show()


"""