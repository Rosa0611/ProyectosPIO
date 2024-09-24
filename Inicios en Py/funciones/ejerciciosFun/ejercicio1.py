#crear una calculadora con diccionario

def suma (x,y):
    return x + y

def resta (x,y):
    return x - y

def dividir (x,y):
    if y != 0:
     return x / y
    else: 
        return "no se puede dividir por cero"

def multiplicar (x,y):
    return x * y

def exponente (x,y):
    return x ** y

#programa principal
def menu ():
 print ("1. suma ")
 print ("2. resta ")
 print ("3. dividir ")
 print ("4. multiplicar ")
 print ("5. exponente ")
 print ("6. salir ")
 print ("1. suma ")

#diccionario
operaciones = {
    "1":("suma",suma),
    "2":("resta",resta),
    "3":("dividir",dividir),
    "4":("multiplicar",multiplicar),
    "5":("exponente",exponente),

}


while True:
    
    menu ()
    opcion = int(input("Selecciona una operacion: "))

    if opcion in operaciones: 
        numero1 = float(input("ingrese el primer valor"))
        numero2 = float(input("ingrese el segundo valor"))

        resultado = operaciones[opcion](numero1, numero2)

        print (f"El resultado es: {resultado}")

    elif opcion == 6:
        print ("saliendo...")
        break
    else:
        print ("Error: operacion invalida")
 



