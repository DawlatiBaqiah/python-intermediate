import random

def main():
    """Start a colour guessing game"""
    print("Guess the colour")

    rainbow = [
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "indigo",
        "violet",
    ]

    x = random.choice(rainbow)
    print(x)
    guess = None
    while x != guess:

        guess = str(input("what colour am i thinking of"))

        if x == guess:
            print("You Guessed {}. Congratulations you got it right!".format(guess))
            break
        else:
            print("You guessed{}. Unfortunately its wrong. Try Again!" .format(guess))

main() 