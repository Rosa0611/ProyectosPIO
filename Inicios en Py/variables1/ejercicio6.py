#encontrar hipotemusa
from math import sqrt

cateto1 = float(input("ingrese el valor del cateto 1: "))
cateto2 = float(input("ingrese el valor del cateto 2: "))

hipotenusa = (cateto1 ** 2) + (cateto2 ** 2)
resultado = sqrt(hipotenusa)

print (f"el valor de la hipotenusa del rectangulo es {resultado}")