from games import number_guessing, higher_lower, silly_game

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
        higher_lower()

    elif user_choice == 3:
        silly_game()

    else: 
        print("Introduce una opción válida")


keep_playing = True

while keep_playing:
    play_chipiado()

    kp = input("Keep playing?")

    if kp == "n":
        keep_playing = False