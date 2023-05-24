from random import randint

print("Welcome to the guessing game!")

def play():
    computer_guess = randint(1, 10)
    user_guess = int(input("Guess a number: "))
    