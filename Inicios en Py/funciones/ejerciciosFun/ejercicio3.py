#tablas de multiplicar

def tablaMultiplicar (numero):
    for i in range (1, 11):
        print (f"{numero} x {i} = {numero * i}")

numero = int(input("Ingrese el numero que desea multiplicar: "))

tablaMultiplicar(numero)
