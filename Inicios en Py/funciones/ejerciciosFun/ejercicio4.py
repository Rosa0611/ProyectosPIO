#ejercicio de calificaciones: 
'''Crea un sistema que permita al usuario ingresar las calificaciones de varios estudiantes y calcule el promedio general. Usa condicionales para validar si el estudiante ha aprobado o reprobado.'''

def calcularPromedio (calificaciones, cantidad):
    return sum(calificaciones)/ cantidad

def estadoEstudiante (promedio):
    if promedio >= 4:
        return "Aprobado"
    else: 
        return "Reprobado"

calificaciones = []

cantidad = int (input("Cuantas calificaciones desea ingresar: "))

contador = 0

while contador < cantidad:
    calificacion = float(input("Ingrese la calificacion: "))
    if (calificacion in range(0,6)):   
        calificaciones.append(calificacion)
        contador += 1
    else:
        print ("Ingresaste la calificacion incorrecta, el rango es de 0 -5")
promedio = calcularPromedio(calificaciones, cantidad)
estado = estadoEstudiante(promedio)

print (f"Promedio: {promedio} \nEstado: {estado}")