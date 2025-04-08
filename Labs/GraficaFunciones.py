#Para graficar se usa el paquete Matplotlib
#Para importar un paquete se usa from nombrePaquete import funcionTrabajada


from matplotlib import pyplot
'''
Funciones lineales f(x)=4x+1
Obtener la imagen para f(2) y f(-1)
'''
'''
def f1(x):
    return 4*x+1
#Grafica de la función
#Valores del eje x de la gráfica, se usa range y genera valores entre dos puntos
x=range(-100,100)

#Comando plot(x,y) o ploy(x,f(x)) , también se puede pasar un tercer parámetro
#Tercer parámetro plot(x,y,"g") es el color debe ser la letra en minuscula del color en ingles
#Si se coloca un caracter la gráfica se hará de esos carácteres
pyplot.plot(x,[f1(i) for i in x],"y3")

#Para establecer colores de los ejes
pyplot.axhline(0,color="blue")
pyplot.axvline(0,color="blue")
#Titulo de la grafica
pyplot.title("Función lineal",fontsize=10, color="red")
#Etiqueta a los ejes
pyplot.xlabel("Eje x")
pyplot.ylabel("Eje y")

#Se puede agregar una maya punteada "dashe"
pyplot.grid(color="gray",linestyle="dashed")
#Para mostrar la gráfica se usa .show()
pyplot.show()
'''

#Función cuadratica 3*x**2+5*x-2  se usa ** para elevar al cuadrado
def f2(x):
    return 2*(x**2)+5*x-2
#Crear gráfica

#Valores del eje x
x = range(-10,10)
pyplot.plot(x,[f2(i) for i in x])
pyplot.title("Funcion cuadrática",fontsize=10, color="red")
pyplot.axhline(0,color="blue")
pyplot.axvline(0,color="blue")
pyplot.xlabel("Eje x")
pyplot.ylabel("Eje y")
pyplot.grid(color="gray",linestyle="dashed")
pyplot.show()




