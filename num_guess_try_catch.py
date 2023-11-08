#!usr/bin/env python3
# Created By: Marli Peters
# Date: Nov. 7, 2023
# This program asks the user to guess a
# number then tells user if the guess was correct. If the user
# enters something other than an integer the program
# will catch it.

import random


def main():
    # get user guess
    guess_string = str(input("Guess random number between 0 and 9: "))
    print("")

    # setting random number
    answer = random.randint(0, 9)

    # check if guess is correct
    try:
        guess_int = int(guess_string)

    except:
        print("Please enter a valid integer.")

    else:
        if guess_int != answer:
            print("Your guess was incorrect!")

        elif guess_int == answer:
            print("Your guess was correct!")

    finally:
        print("The correct number was {}.".format(answer))


if __name__ == "__main__":
    main()
