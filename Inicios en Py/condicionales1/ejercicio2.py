#verificar notas >= 60 aprueba puntos posibles 100
import math

calificacion = float(input ("digite la nota: "))
calificacion = round (calificacion)
print (calificacion)

if calificacion >= 60 and calificacion <= 100:
    print ("el estudiante aprobo")
elif calificacion >= 0 and calificacion < 60 :
    print ("el estudiante reprobo")
else:
    print ("la calificacion es invalida")