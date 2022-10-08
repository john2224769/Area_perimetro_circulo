# Programa No. 1: Area y Perimetro de un circulo

import math

print("-----------------------------")
print("------ Area - Perimetro ------")
print("-----------------------------")

#input
r=input("Digite el valor del radio ")
r=int (r)
print(" ")

#processing
A=math.pi*r*r
P=2*math.pi*r

#output
print("-----------------Resultados-------------------")
print(" ")
print("El area es: "+str(A))
print("El perimetro es: "+str(P))
print(" ")