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
    print(f"Actualizando pelicula con id {id_actualizar}")
    for i, pelicula in enumerate (peliculas):
        if id_actualizar == i: 
            print(f"Comparando con pelicula {i}")

            try:
            print ("Pelicula Encontrada")
            nombre = input(f"Nombre de la película {pelicula['nombre']}: ")
            descripcion = input(f"Descripción: ")
            estreno = int(input(f"Fecha de estreno (dd-mm-aaaa): "))
            genero = input(f"Género: ").split(',')
            clasificación = input(f"Clasificación: ")
            duracion = input(f"Duración: ")
            director = input(f"Director: ").split(',')
            actores = input(f"Actores principales: ").split(',')
            print("Actualizando pelicula")

             # Actualizar la película
            pelicula['nombre'] = nombre
            pelicula['descripcion'] = descripcion
            pelicula['estreno'] = estreno
            pelicula['genero'] = [g.strip() for g in genero]
            pelicula['clasificación'] = clasificacion
            pelicula['duracion'] = duracion
            pelicula['director'] = [d.strip() for d in director]
            pelicula['actores'] = [a.strip() for a in actores]
                    
            print("Película actualizada exitosamente.")
            return
                
                except IndexError:
                    print("No se encontró la película con el índice proporcionado.")
                except ValueError:
                    print("Error: La duración debe ser un número entero.")

def crear_una_pelicula(peliculas):
    """
    Permite crear una nueva película en la lista de películas.
    
    Solicita al usuario los datos de la película a crear, y los agrega a la lista.
    
    Si hay un error en la entrada de datos, muestra un mensaje de error.
    """
    print("Crear pelicula")
    
    # Solicitar los datos de la película
    try:
        nombre = input(f"Ingrese Nombre de la película: ")
        descripcion = input(f"Ingrese nueva Descripción: ")
        estreno = input(f"Ingrese nueva Fecha de Estreno: ")
        genero = input(f"Ingrese nuevo Género (separado por comas): ").split(',')
        clasificacion = input(f"Ingrese nueva Clasificación: ")
        duracion = int(input(f"Ingrese nueva Duración (en minutos): "))
        director = input(f"Ingrese nuevo Director (separado por comas): ").split(',')
        actores = input(f"Ingrese nuevos Actores (separado por comas): ").split(',')
        
        # Crear la nueva película
        nueva_pelicula = {
            'nombre': nombre,
            'descripcion': descripcion,
            'estreno': estreno,
            'genero': [g.strip() for g in genero],
            'clasificación': clasificacion,
            'duracion': duracion,
            'director': [d.strip() for d in director],
            'actores': [a.strip() for a in actores]
        }
        
        # Agregar la nueva película a la lista
        peliculas.append(nueva_pelicula)
        print("Película agregada exitosamente.")
    except ValueError:
        print("Error: La duración debe ser un número entero.")

def eliminar_pelicula(id_eliminar,peliculas):
    try:
        peliculas.pop(id_eliminar)
        print("Película eliminada exitosamente.")
    except IndexError:
        print("No se encontró la película con el índice proporcionado.")
    
def buscar_por_id(id_buscar, peliculas):
    try:
        pelicula = peliculas[id_buscar]
        tabla = PrettyTable()
        tabla.field_names = ["Atributo", "Valor"]

        tabla.add_row(["Nombre", pelicula['nombre']])
        #tabla.add_row(["Descripción", pelicula['descripcion']])
        tabla.add_row(["Estreno", pelicula['estreno']])
        tabla.add_row(["Género", ', '.join(pelicula['genero'])])
        tabla.add_row(["Clasificación", pelicula['clasificación']])
        tabla.add_row(["Duración (min)", pelicula['duracion']])
        tabla.add_row(["Director", ', '.join(pelicula['director'])])
        tabla.add_row(["Actores", ', '.join(pelicula['actores'])])

        print(tabla)
    except IndexError:
        print("No se encontró la película con el índice proporcionado.")
    except Exception as e:
        print(f"Error al buscar la película: {e}")



# Menú principal
while True:
    print("\n----- Menú -----")
    print("1. Mostrar todas las películas")
    print("2. Crear una nueva película")
    print("3. Actualizar una película")
    print("4. Eliminar una película")
    print("5. Buscar una película por ID")
    print("6. Salir")
    
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        mostrar_todas_peliculas(peliculas)
    elif opcion == '2':
        crear_una_pelicula(peliculas)
    elif opcion == '3':
        try:
            id_actualizar = int(input("Ingrese el índice de la película a actualizar: "))
            actualizar_una_pelicula(id_actualizar, peliculas)
        except ValueError:
            print("Dato no válido. Ingrese un número entero.")
    elif opcion == '4':
        try:
            id_eliminar = int(input("Ingrese el índice de la película a eliminar: "))
            eliminar_pelicula(id_eliminar, peliculas)
        except ValueError:
            print("Dato no válido. Ingrese un número entero.")
    elif opcion == '5':
        try:
            id_buscar = int(input("Ingrese el índice de la película a buscar: "))
            buscar_por_id(id_buscar, peliculas)
        except ValueError:
            print("Dato no válido. Ingrese un número entero.")
    elif opcion == '6':
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Por favor, intente de nuevo.")
        



