edad = int(input("Ingrese la edad: "))
tieneLicencia = True

if edad >= 18 and tieneLicencia == True and edad < 80:
    print("La persona puede conducir")
else:
    print("La persona no puede conducir")