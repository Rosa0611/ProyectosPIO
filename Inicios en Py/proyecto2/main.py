peliculas = [
    {
        "nombre": "Deadpool & Wolverine", 
        "descripcion": "En esta esperada colaboración, Deadpool se une a Wolverine para enfrentar amenazas nunca antes vistas, mezclando acción y humor irreverente. La película sigue a los dos antihéroes mientras forman una extraña alianza, combatiendo enemigos tanto del pasado como del presente.",
        "estreno": "03-10-2024",
        "genero": "Acción, Ciencia Ficción, Superhéroes", 
        "clasificación": "Mayores de 15 años", 
        "duracion": "2 horas 15 minutos (aproximadamente)", 
        "director": "Shawn Levy", 
        "actores": "Ryan Reynolds, Hugh Jackman"
    }
]

def mostrarPelicula(peliculas, nombrePelicula):
    print("-----------Lista de Peliculas---------")
    for pelicula in peliculas:
        if pelicula["nombre"].lower() == nombrePelicula.lower():
            print(f"Nombre: {pelicula['nombre']}")
            print(f"Descripción: {pelicula['descripcion']}")
            print(f"Estreno: {pelicula['estreno']}")
            print(f"Género: {pelicula['genero']}")
            print(f"Clasificación: {pelicula['clasificación']}")
            print(f"Duración: {pelicula['duracion']}")
            print(f"Director: {pelicula['director']}")
            print(f"Actores: {pelicula['actores']}")
            print("---------------------------------")

def actualizarPelicula(id_actualizar, peliculas):
    for i, pelicula in enumerate (peliculas):
        if id_actualizar == i: 
            print ("Pelicula Encontrada")
            nombre: input(f"Nombre de la película {pelicula['nombre']}: ")
            descripcion: input(f"Descripción: ")
            estreno: int(input(f"Fecha de estreno (dd-mm-aaaa): "))
            genero: input(f"Género: ").split(',')
            clasificación: input(f"Clasificación: ")
            duracion: input(f"Duración: ")
            director: input(f"Director: ").split(',')
            actores: input(f"Actores principales: ").split(',')
        



