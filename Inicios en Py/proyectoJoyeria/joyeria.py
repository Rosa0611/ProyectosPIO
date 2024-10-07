#Lista de productos
import os
productos = [
    {"nombre":"Anillo de Diamantes", "precio":10000000, "cantidad":5},
    {"nombre":"Anillo de Oro", "precio":5000000, "cantidad":5},
    {"nombre":"Anillo de Plata", "precio":1000000, "cantidad":12},
    {"nombre":"Anillo de Cuarzo", "precio":100000, "cantidad":8}

]

carrito = []

def limpiaPantalla ():
    if os.name == 'nt':
        os.system('cls') #Limpiar terminal en windows

def mostrarProductos ():
    limpiaPantalla()
    print ("------Menu de productos------")
    for i, producto in enumerate (productos):
        print(f"{i+1}.{producto['nombre']}-precio ${producto['precio']} - cantidad {producto['cantidad']}")

def agregaralCarrito ():
    limpiaPantalla()
    mostrarProductos()
    try:
        opcion = int(input("Digite la opcion del producto que desea agregar: "))
        if 1<=opcion<= len(productos):
            cantidad = int(input("Digite la cantidad que desea comprar: "))
            producto = productos [opcion-1]
            if cantidad > producto["cantidad"]:
                print ("no hay suficientes productos")
            else:
                productos[opcion-1]['cantidad']-= cantidad
                carrito.append ({"nombre":producto ['nombre'], "precio": producto['precio'], "cantidad": cantidad})
                print(f"Felicidades!! Añadiste {cantidad['cantidad']},{producto['nombre']} de manera exitosa")

        else:
            print("Opcion invalidad")

    except Exception as e:
        print ("Se ha producido un error", e)

def mostrarCarrito ():
    limpiaPantalla()
    if carrito:
        print ("Carrito de compras")
        for i, item in enumerate  (carrito, 1):
            print(f"{i}.producto:{item['nombre']}- ${item['precio']} - cantidad: {item['cantidad']}")
        else:
            print("El carrito está vacio")


def calcularTotal ():
    total= sum(item['precio']*item['cantidad'] for item in carrito)
    print (f"El total a pagar es: ${total} ")


def finalizarCompra ():
    limpiaPantalla()
    mostrarCarrito()

    if carrito:
        calcularTotal()
        confirmar = input("Desea finalizar su compra (Si/No): ")

        if confirmar.lower() == "si":
            carrito.clear()
            print ("La compra fue realizada exitosamente")
        else:
            print ("La compra fue cancelada")
    else:
        print ("No hay productos en el carrito")


def main ():
    while True:
        limpiaPantalla()
        print ("-------- Menu Joyeria --------")
        print ("1. Mostrar produtos disponibles ")
        print ("2. Añadir produtos al carrito ")
        print ("3. Mostrar el carrito ")
        print ("4. Finalizar la compra ")
        print ("5. Salir del programa ")

        try:
            opciones = {
                1: mostrarProductos,
                2: agregaralCarrito,
                3: mostrarCarrito,
                4: finalizarCompra  
            }
            seleccion = int(input ("Digite la opcion deseada: "))
            if seleccion in opciones:
                opciones[seleccion]()
                input("Presione enter para continuar")
            elif seleccion == 5:
                break
        except ValueError:
            print ("La entrada es invalida, por favor digite un numero")
            input("Presione enter para continuar")
        except Exception:
            print ("Se ha presentado un error")
            input("Presione enter para continuar")

main()



