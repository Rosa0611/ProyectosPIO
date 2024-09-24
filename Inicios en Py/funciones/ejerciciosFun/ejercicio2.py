def agregarEstudiantes(estudiantes):
    
    documento = input("ingrese el documento:" )
    tipoDocumento = input("ingrese el tipo de documento (cc/ti): ").lower()
    nombre = input("ingrese el nombre: ").capitalize()
    apellidos = input ("ingrese los apellidos: ").capitalize()

    if buscarEstudiante (estudiantes, documento):
        print ("Error: el estudiante ya existe")
        return

    if tipoDocumento == "cc" or tipoDocumento == "ti":
        estudiantes.append({"documento":documento, "tipoDocumento":tipoDocumento, "nombre": nombre, "apellidos":apellidos})
        print ("estudiante guardado con exito")
    else: 
        print ("Error: tipo de documento no valido")
    

def mostrarEstudiantes(estudiantes):
    if not estudiantes:
        print ("no hay estudiantes registrados")
    else:
        for estudiante in estudiantes:
            print(f"documento: {estudiante["tipoDocumento"]}{estudiante["documento"]} - {estudiante["nombre"]} {estudiante["apellidos"]}")
    

def eliminarEstudiantes(estudiantes):
    documento_a_eliminar = input("ingrese el documento a eliminar: ")
    estudiante_a_eliminar = buscarEstudiante (estudiantes, documento_a_eliminar)
    
    if estudiante_a_eliminar:
            estudiantes.remove(estudiante_a_eliminar)
            print ("estudiante eliminado con exito")
    else:

        print ("Error: estudiante no encontrado")


def buscarEstudiante (estudiante, documento_a_buscar):
    for estudiante in estudiantes:
        if documento_a_buscar == estudiante["documento"]:
            return estudiante


def menuEstudiantes():
    print ("1. Agregar estudiante")
    print ("2. Mostrar estudiante")
    print ("3. Eliminar estudiante")
    print ("4. Salir")

estudiantes = []

while True:
    menuEstudiantes()
    opcion = int(input("Elije una opcion: "))

    if opcion == 1:
        agregarEstudiantes(estudiantes)
    if opcion == 2:
        mostrarEstudiantes(estudiantes)
    if opcion == 3:
        eliminarEstudiantes(estudiantes)
    if opcion == 4:
        break
    else:
        print("Error: opcion invalida")
    


