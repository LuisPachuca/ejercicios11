import random

def juego():
    options = ['piedra','papel','tijeras']
    computer_choice = random.choice(options)
    user_choice = input("Elija entre piedra, papel o tijeras: ").lower()

    if user_choice not in options:
        print("Option no valida... Por favor ingrese una opcion valida :)")
        return
    print(f"Eligio la opcion {user_choice} y la computadora eligio la opcion {computer_choice}.")

    if user_choice == computer_choice:
        print("Empate!")
    elif (user_choice == 'piedra' and computer_choice == 'tijeras') or (user_choice == 'papel' and computer_choice == 'piedra') or (user_choice == 'tijeras' and computer_choice == 'papel'):
        print("¡Ganaste!")
    else:
        print("Perdiste. Lo siento :(")

juego()