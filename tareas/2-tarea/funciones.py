from random import randint

def number_guessing():
    computer_guess = randint(1,1)
    user_guess = int(input("Select a number"))

    if user_guess == computer_guess:
        print("You won!")
    else: 
        print("You lost")



def play_chipiado():
    print("Bievnenido a mi play chipiado")

    try: 
        user_choice = int(input("¿Qué quieres jugar? Tenemos 1. juego 1, 2. juego 2, 3. juego 3."))
    except:
        print("Introduce una opción válida")
        return "Error"

    if user_choice == 1:
        number_guessing()

    elif user_choice == 2:
        print("Elegiste el juego 2")

    elif user_choice == 3:
        print("Elegiste el juego 3")

    else: 
        print("Introduce una opción válida")


keep_playing = True

while keep_playing:
    play_chipiado()

    kp = input("Keep playing?")

    if kp == "n":
        keep_playing = False