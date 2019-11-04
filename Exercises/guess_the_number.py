# This is a Guess the Number game

import random

# Use the imported random function to generate a random number between 1 and 20
secret_number = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

# Ask the player to guess 6 times
for guesses_taken in range(1, 7):
    # Modified from the textbook example to only one line of code.
    guess = int(input("Take a guess: "))

    if guess < secret_number:
        print('Your guess is too low.')
    elif guess > secret_number:
        print('Your guess is too high.')
    else:
        break # This condition is the correct guess.

if guess == secret_number:
    print('Good job! You guessed my number in ' + str(guesses_taken) + ' guesses!')
else:
    print('Sorry. The number I was thinking of was ' + str(secret_number))
