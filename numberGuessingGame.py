#number guessing game

import random

def guess(x):
    number = random.randint(1,x)

    guessed = 0

    while guessed != number:
        print("Guess a number between 1 and ",x)
        guessed = int(input())

        if guessed < number:
            print("The entered number is too low! Guess again.")

        elif guessed > number:
            print("The entered number is too high! Guess again.")

        else:
            print("Correct Guess!")

def computer_guess(x):
    start = 1
    end = x
    f = ''

    while f != 'f':
        if start != end:
            guess = random.randint(start, end)

        else: guess = start 

        f = input(f'Is {guess} too high (H), too low (L), or correct (F)?? ').lower()

        if f == 'h': end = guess -1

        elif f == 'l': start = guess + 1

        print('The computer guessed correctly!')

guess(11)