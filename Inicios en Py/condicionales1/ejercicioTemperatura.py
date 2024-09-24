temperatura = float(input("ingrese la temperatura actual: "))
llueve = input(" Esta lloviendo? (si/no)").lower()

if temperatura < 15:
    if llueve == "SI":
        print ("Usa un abrigo y paragua")
    else:
        print ("Usa un abrigo")
elif 15 <= temperatura <= 25:
    if llueve == "SI":
        print ("lleva un paraguas")
    else:
        print ("Usa ropa ligera")
else:
    print ("Usa ropa fresca")

