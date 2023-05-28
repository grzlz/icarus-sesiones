from games import number_guessing, higher_lower, silly_game

def play_chipiado():
    print("Play Chipiado gives you the wamest welcome!")
    try: 
        user_choice = int(input("Choose one of our three wonderful games. (1/2/3)"))
    except:
        print("Please choose a valid option.")
        return "Error"
    if user_choice == 1:
        number_guessing()
    elif user_choice == 2:
        higher_lower()
    elif user_choice == 3:
        silly_game()
    else: 
        print("Please choose a valid option.")

keep_playing = True
while keep_playing:
    play_chipiado()
    kp = input("Do you want to keep playing?")
    if kp == "n":
        keep_playing = False
        