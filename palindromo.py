pala = input("Ingresa algunas palabras separadas por espacios: ")

palabras = pala.split()

for palabra in palabras:
    if palabra == palabra[::-1]:
        print(palabra, 'es palíndroma')
    else:
        print(palabra, 'no es palíndroma')
