'''
Funciones
'''
#Definir una función se utiliza la palabra def nombre () en paréntesis son las entradas
#Siempre definir la función antes de usarla


#Caso 1 sin datos
def saludo ():
    print("Caso 1.\nHola Axel")  

#Caso 2, recibe un parámetro
def saludo2(nombre):
    print("\nCaso 2.\nHola",nombre)
    
#Caso 3, más de un parámetro, cada parámetro se sepra con , y si falta algun parámetro da error
def saludo3(nombre,apellidoPaterno):
    print("\nCaso 3.\nHola"+" "+nombre+" "+apellidoPaterno)


#Si no sabemos cuántos parámetros son, se utiliza *NombreParametro, el * nos indica que lo que viene  a continuación es variable

def alumnosED(*nombres):
    print("Alumno de ED",nombres[5])
    
def llaveValor(llave1,llave2,llave3):
    print("El nombre es",llave1)

#Una vez definida, debemos llamar a la función poniendo su nombre y los parentesis con las entradas
saludo()
saludo2("Axel Daniel")
saludo3("Axel","Becerril")
alumnosED("Axel","Tania","Michel","Daniel","Ana","Emiliano","Isabel")

#Argumentos tipo llave/valor
'''
30125 - Axel
56981 - Tania
63980 - Michel
45698 - Daniel
49765 - Ana
03249 - Emiliano
79301 - Isabel
'''
llaveValor(llave1="Axel",llave2=" Tania", llave3= "Michel")

'''Retorno de valores
Se usa la palabra return nombre  para que regrese un dato la función 
'''
def suma(a,b):
    resultado=a+b
    return resultado
print("\nRetorno de un valor de una función")
print(suma(5,15))


#Regresar más de un valor debemos poner  las variables en orden de como las fuimos poniendo en la funcion
def calculadora(x,y):
    suma = x+y
    resta = x-y
    multiplicacion = x*y
    division = x/y #// division entera, / división con decimales
    return suma, resta, multiplicacion, division
suma, resta, multiplicacion, division = calculadora(10,5)
print("\nDatos múltiples")
print(suma)
print(resta)
print(multiplicacion)
print(division)


'''
Funciones lineales f(x)=4x+1
Obtener la imagen para f(2) y f(-1)
'''
def f1(x):
    return 4*x+1

#f(2)=9
print("\nFunción lineal f(2)")
print(f1(2))

#f(-1)
print("\nFunción lineal f(1)")
print(f1(-1))

'''
Tupla en python
'''

#Es una estructura, es una estructura con elementos ordenados que no pueden cambiar

Tupla=(1,2,3)
