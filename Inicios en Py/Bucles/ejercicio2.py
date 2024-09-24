#"adivinar la palabra"
palabraAdivinar = "Hola programadores"

intentos_max = 4

intento = 0

while intentos_max != intento:
    print ("******Juego Adivinar*****")
    print (f"Tienes {intentos_max} intentos te quedan {intentos_max - intento}")

intentoAdivinar = input(f"ingrese la palabra: ")

if intentoAdivinar == palabraAdivinar:
    print ("ganaste")

