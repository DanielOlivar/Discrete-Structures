from matplotlib import pyplot
from math import sqrt
'''
Sea f(x)=raiz(x) y g(x = x+1)
Encontrar fog
y gof

'''
def f1(x):
    return sqrt(x+2)

#Valores del eje x
x = range(-2,50)
pyplot.plot(x,[f1(i) for i in x])
pyplot.title("AProblema 10",fontsize=10, color="black")
pyplot.axhline(0,color="red")
pyplot.axvline(0,color="red")
pyplot.xlabel("Eje x")
pyplot.ylabel("Eje y")
pyplot.grid(color="gray",linestyle="dashed")
pyplot.show()

