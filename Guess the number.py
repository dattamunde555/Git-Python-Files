# Guess the number game

import random
print('I have randomly picked a number between 1 and 100')
number = random.randint(1,100)
guesses = 1
user = int(input('What is the number? '))
while user != number:
    if user > number:
        user = int(input('Too high. Guess again: '))
    if user < number:
        user = int(input('Too low. Guess again, idiot: '))
    guesses += 1
print('\nYou got it. The number was',number)
print('It took you',guesses,'tries to guess it.')
