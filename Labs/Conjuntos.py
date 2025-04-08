#Crear un conjunto en python

#En python los conjuntos se representan cmediante la estructura SET

#Definición de un conjunto 
vocales = {'a','e','i','o','u','a','e'} 
print(vocales) #Nunca se imprimen en orden
print(type(vocales)) #Imprime SET porque es un conjunto

#Añadir elementos a un conjunto

paises = {'México', 'Argentina','Colombia','Uruguay'}

print(paises)

paises.add('Chile')

print(paises)

#Combinar conjuntos

A={1,2,3,4,5}
B={6,7,8,9,10}
print(A)
A.update(B)
print("Combinando elementos de A y B: ",A) 

#Eliminar elementos de un conjuntos Nombre.remove(valor)
B.remove(10)
print(B)

#Vacíar totalmente el conjunto Nombre.clear()
print(A)
A.clear()
print(A) 


#Definir un conjunto vacío
C={} #Esta mal, es la definición de un diccionario.
print(type(C))
#Para definirlo es mediante su constructor Nombre=set()
ConjuntoVacio=set()
print(type(ConjuntoVacio))


#OPERACIONES CON CONJUNTOS

A={1,2,3}

#SEA EL CONJUNTO B

B={4,5,6,}

'''
UNIÓN
SE REALIZA CON EL OPERADOR | Y ESO REGRESA  UN CONJUNTO QUE CONTIENE 
LOS ELEMENTOS QUE SE ENCUENTREN EN AL MENOS UNO DE LOS DOS CONJUNTOS INVOLUCRADOS EN LA OPERACION
'''

#Sea el conjunto U
U = A|B
print(U)


''' Interseccion 
Opera con el símbolo &
Esto retorna un nuevo conjunto cob los elemtnos que pertenecena a A y B.

'''

#Sea el conjunto C

C={1,2,3,4,5}

#Sea el conjunto D

D={4,5,6,7,8}

I= D&C

print(I)

'''
DIFERENCIA
Retorna un conjunto que contiene los elementos de A que no están en B
Se usa el operador -   '''


#Sea el conjunto E
E={1,2,3,4}

#Sea el conjunto F
F={2,3}

D1=E-F

print(D1)

D2=F-E
print(D2)


'''Iguakdad de conjuntos
Dos conjuntos son iguales si y solo si contienen los mismos elementos'''


G={'a','b','c'}
H={'c','b','a','f'}

#En pyton podemos comparar objetos con el operador ==

if G==H:
    print("Los conjuntos C y H son iguales")
else:
    print("Los conjuntos G y H no son iguales.")

'''Subconjunto
Se dice que A es un subconjunto de B cuando todos los elementos del conjunto 
B estan en el conjunto A
Se usa el método issubset()
Se usa el . antes para acceder al método '''


R={1,2,3,4}
J={7,15}

if J.issubset(R):
    print("El conjunto J si es un subconjunto")
else:
    print("El conjunto J no es un subconjunto de R")
    
