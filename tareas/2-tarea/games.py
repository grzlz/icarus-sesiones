from random import randint

def number_guessing():
    computer_guess = randint(1,1)
    user_guess = int(input("Select a number"))

    if user_guess == computer_guess:
        print("You won!")
    else: 
        print("You lost")