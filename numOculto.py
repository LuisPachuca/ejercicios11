import random

number = random.randrange(1,50)
guess = int(input("Coloque un numero entre el 1 y el 50: "))

while guess != number:
    if guess < number:
        print("Necesitas colocar un numero mas alto, vuelve a intentarlo")
        guess = int (input("\n Ingrese un numero entre 1 y 50: "))
    else:
        print("Ingrese un numero mas bajo, vuelva a intentarlo")
        guess = int (input("\n Ingrese un numero entre 1 y 50: "))

        print("Ingreso el numero correcto, bravo!! :D")

