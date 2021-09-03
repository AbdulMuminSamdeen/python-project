"""
File: guessmynumber.py
----------------------
This program checks if a user's guess of a number matches that guessed by the computer
"""

#import random
# use code below  to generate a random integer between 30 and 50 for example
#print(random.randint(30, 50))

# ********************************** YOUR CODE GOES BELOW HERE *********************************************************
from random import randint

secret_key = randint(30, 50)

print("I am thinking of a number between 30 and 50")

while True:
    try:
        # prompt the user to enter a number
        user_input = int(input(" Enter a guess : "))
        guessed = True if user_input == secret_key else False

# check if the user guessed correctly
        if guessed:
            print( "congratulation! the number was {secret_key}")
            break
        else:
            if user_input < secret_key:
                print("your Guess was too low")
            else:
                print("your Guess was too high")
# if the user makes an invalid entry
    except(TypeError, ValueError):
        print("please enter a number")

