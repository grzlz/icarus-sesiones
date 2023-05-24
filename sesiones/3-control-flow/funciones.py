import random

def guess_a_number():
    print("Hello, you're gonna guess my number")
    number_c = random.randint(1,99)
    game = True
    while game:
        number_u = input("Which number are you guessing? ")
        if number_u.isnumeric() == True:
            number_u = int(number_u)
            if number_u < 100:
                if number_u == number_c:
                    print("You guess my number \\ End Game")
                    game = False
                else:
                    print("You did not guess my number")
                    game_o = input("Wanna play again? ")
                    if game_o.lower() == "no":
                        print("This is the end \\ Game over")
                        game = False
            else:
                print("This is not a valid number")
        else:
            print("This is not a number")

