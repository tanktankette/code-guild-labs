from random import randrange
from time import sleep
from os import system

play = True

while play:
    system("clear")
    upper_limit = int(input("""First off, what range of numbers do you want me to
    pick a number from, from 1 to...: """))

    number = randrange(1, upper_limit)

    guess_number, guess_current = 0, -1

    while guess_current != number:
        guess_number += 1
        guess_current = int(input(f"Guess #{guess_number}: "))
        print("Hmm...")
        sleep(.5)
        if(guess_current < number):
            print("Too low!")
        elif(guess_current > number):
            print("Too high!")

    print(f"Congrats, that's correct! You got it in {guess_number} guesses.")
    play = input("Would you like to play again (y/n): ").upper() == "Y"
