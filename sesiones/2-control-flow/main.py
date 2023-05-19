from random import randint 

print("Bienvenido al juego de adivinar el número. Yo escogeré un número del 1 al 100 y tú tendrás la oportunidad de adivinar.")
user_input = input("Introduce un número:")

if user_input.isnumeric() == True:
    computer_guess = randint(1,1)
    if int(user_input) == computer_guess:
        print("You guessed correctly!")
    else:
        print("Try again!")
else: 
    print("Ese no es un número entero.")