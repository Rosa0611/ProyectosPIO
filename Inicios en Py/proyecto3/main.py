#aplicacion de cajero automatico

usuario1 = {
        'nombre': 'juan',
        'contrasena': '1234',
        'saldo': 1000
    },
usuario2= {
        'nombre': 'pedro',
        'contrasena': '4321',
        'saldo': 2000
    },
usuario3= {
        'nombre': 'maria',
        'contrasena': '1111',
        'saldo': 3000
    }

usuarios = [usuario1, usuario2, usuario3]


def autenticarUsuario(nombre: str, contrasena: str) -> bool:
    """Autenticar un usuario."""
    usuario = next((u for u in usuarios if u["nombre"] == nombre), None)
    if usuario and usuario["contrasena"] == contrasena:
        return True
    return False

    
def consultarSaldo (usuario):
    print ("Consultando saldo de", usuario.get ('nombre'))
    saldo = usuario.get ('saldo')
    print ("Saldo de", usuario.get ('nombre'), "es de", saldo)
    return saldo


def retirarDinero (usuario, monto):
    print ("retirando", monto, "de la cuenta de", usuario.get ('nombre'))
    saldo = usuario.get ('saldo')
    print ("Saldo actual:", saldo)
    if saldo >= monto:
        usuario['saldo'] = saldo - monto
        print ("nuevo saldo:", usuario.get ('saldo'))
        return (f"se ha retirado ${monto} de tu cuenta")
    print ("no tienes saldo suficiente")
    return "no tienes saldo suficiente"

def depositarDinero (usuario, monto):
    if monto > 0:
        saldo = usuario.get ('saldo')
        usuario['saldo'] = saldo + monto
        return (f"se ha depositado ${monto} en tu cuenta")
    return "el monto debe ser mayor a 0"

#Cambia la contrasena del usuario si coincide con la actual
def cambiarContrasena (usuario):
    contrasenaActual = input("ingrese la contrasena actual: ")
    if contrasenaActual == usuario.get ('contrasena'):
        nuevaContrasena = input("ingrese la nueva contrasena: ")
        usuario['contrasena'] = nuevaContrasena
        return "contrasena cambiada"
    return "contrasena incorrecta"
# creacion de menu que me va permitir autenticar si el usuario esta creado y luego me va permitir revisar las opciones del cajero

def menu ():
    while True:
        nombre = input("ingrese su nombre: ")
        if nombre.lower() == "exit":
            break
        contrasena = input("ingrese su contrasena: ")
        autenticado = autenticarUsuario (nombre, contrasena)
        if autenticado:
            print(f"bienvenido {nombre}!")
            break
        print ("contrasena incorrecta, intentelo de nuevo")
    print("autenticado", autenticado)
    while True:
        print("\n----- MENU DE OPCIONES -----")
        print("1. consultar saldo")
        print("2. depositar dinero")
        print("3. retirar dinero")
        print("4. salir")
        try:
            seleccion = int(input("ingrese una opcion: "))
            print("seleccion:", seleccion)
            if seleccion == 1:
                print(f"tu saldo es: ${consultarSaldo (usuarios[nombre])}")
            elif seleccion == 2:
                monto = int(input("ingrese el monto a depositar: "))
                print("monto a depositar:", monto)
                print(depositarDinero (usuarios[nombre], monto))
            elif seleccion == 3:
                monto = int(input("ingrese el monto a retirar: "))
                print("monto a retirar:", monto)
                print(retirarDinero (usuarios[nombre], monto))
            elif seleccion == 4:
                print("hasta pronto")
                break
        except Exception as e:
            print("se ha presentado un error")
            print(e)
menu()
            