from random import randint

def random_number_game():
    keep_playing = True
    while keep_playing == True:
        print("Welcome to the number guessing game!")
        computer_choice = randint(1,10)
        user_guess = int(input("Guess a number between 1-10"))
        if user_guess == computer_choice:
            print("Your guess is correct.")
        else:
            print("Your guess is incorrect.")
        user_choice = input("Do you want to keep playing? Pres y for yes and n for no.") 
        if user_choice == "n":
            keep_playing = False