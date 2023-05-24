from random import randint

print("Welcome to the guessing game!")

def play():
    computer_guess = randint(1, 1)
    user_guess = int(input("Guess a number: "))

    if user_guess == computer_guess:
        print("You won!")

    else:
        print("You lost!")

keep_playing = True

while keep_playing:
    play()
    keep_playing_response = input("Do you want to keep playing? (y/n): ")
    if keep_playing_response == "n":
        keep_playing = False
        print("Goodbye!")
