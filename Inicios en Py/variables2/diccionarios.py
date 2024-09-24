'''Diccionario
Coleccion de datos desordenados de pares (clave-valor), donde cada clave debe ser unica y esta asociada a un valor
se utilizan para representar relaciones de datos como una tabla'''

#definicion de diccionario
miDiccionario = {
    "nombre":"Rosa",
    "apellido": "Rosero",
    "edad": "24"
}

print (miDiccionario)

#Acceder a un valor
print (miDiccionario["edad"])

#Modificar un valor
miDiccionario["edad"] = "18"
print(miDiccionario)

#agregar un dato
miDiccionario["ciudad"] = "Palmira"
print (miDiccionario)

#Eliminar
del miDiccionario["apellido"]
print (miDiccionario)