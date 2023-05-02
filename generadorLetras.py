# Definir la lista de canciones con el nombre, artista y letra
canciones = [
    {"nombre": "Decir adios", "artista": "Cuco", "letra": "El tiempo va a curar nuestro dolor \nY vamos a brindar por lo mejor \nPresiento que un día me olvidarás \nEn mi mente siempre vas ahí a estar..."},
    {"nombre": "Best Disaster", "artista": "Cuco", "letra": "This can be your favorite song \nYou know you’re the one I'm after \nWe can put the world on pause \nThis could be our best disaster..."},
    {"nombre": "Enemigo", "artista": "Enjambre", "letra": "Permite recostarme a tu lado \nSé que mi deseo es raro enemigo \nPero cerca de tu frente es cuando \nMejor respiro \nPermíteme quedarme esta noche contigo..."},
    {"nombre": "DARE", "artista": "Gorillaz", "letra": "You've got to press it on you \nYou've just been thinking \nThat's what you do, baby..."},
    {"nombre": "Dolores", "artista": "Enjambre", "letra": "Si pudiera alterar líneas del tiempo \nVolvería a ese momento \nDonde siempre estabas cerca..."},
]

# Lista de canciones
print("Lista de canciones:")
for i, cancion in enumerate(canciones):
    print(f"{i+1}. {cancion['nombre']} - {cancion['artista']}")

# Opcion
opcion = int(input("Ingrese el número de la canción que desea ver: "))
cancion_seleccionada = canciones[opcion-1]

# Imprimir letra
print(f"Letra de {cancion_seleccionada['nombre']} - {cancion_seleccionada['artista']}:")
print(cancion_seleccionada['letra'])

# Solicitar solo el nombre del artista
artista = input("Ingrese el nombre del artista para ver sus canciones: ")
canciones_artista = [cancion for cancion in canciones if cancion['artista'].lower() == artista.lower()]

# Imprimir la lista de canciones del artista seleccionado
print(f"Canciones de {artista}:")
for i, cancion in enumerate(canciones_artista):
    print(f"{i+1}. {cancion['nombre']}")

# Pedir al usuario que seleccione una canción del artista seleccionado
opcion = int(input("Ingrese el número de la canción que desea ver: "))
cancion_seleccionada = canciones_artista[opcion-1]

# Imprimir letra
print(f"Letra de {cancion_seleccionada['nombre']} - {cancion_seleccionada['artista']}:")
print(cancion_seleccionada['letra'])