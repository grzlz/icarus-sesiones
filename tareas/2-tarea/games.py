from random import randint

def number_guessing():
    computer_guess = randint(1,10)
    user_guess = int(input("Select a number"))

    if user_guess == computer_guess:
        print("You won!")
    else: 
        print("You lost")

def higher_lower():
    computer_guess = randint(1,3)
    user_guess = input("Higher or lower (h/l)? ")
    number_guess = int(input("What number? "))

    if user_guess == "h":
        if number_guess > computer_guess:
            print(f"You won! I wass guessing {computer_guess} and you guessed {number_guess}.")
        else:
            print(f"You lost! I wass guessing {computer_guess} and you guessed {number_guess}.")
    
    else:
        if number_guess < computer_guess:
            print(f"You won! I wass guessing {computer_guess} and you guessed {number_guess}.")
        else:
            print(f"You lost! I wass guessing {computer_guess} and you guessed {number_guess}.")
    
def silly_game():
    print("I'm sorry you just lost, silly.")
