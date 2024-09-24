'''los condicionales nos permiten tomar decisiones dentro de un programa, buscan una verdad o falsedad'''

#mayor de edad
'''
edad = int(input("Ingrese la edad: "))

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("No eres mayor de edad")
'''

#promedios

nota1 = float(input("ingrese la nota 1: "))
nota2 = float(input("ingrese la nota 2: "))
nota3 = float(input("ingrese la nota 3: "))

promedio = ((nota1 + nota2 + nota3) / 3)

if (promedio == 5):
    print (f"Usted tuvo un desempeño excelente en este modulo {promedio}")
elif (promedio >= 4):
    print (f"Usted aprobó el modulo {promedio}")
else: 
    print (f"Usted reprobo el modulo {promedio}")
