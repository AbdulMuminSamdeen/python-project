"""
File: khansole_academy.py
-------------------------
Khansole Academy is a program that teaches users how to add by asking users to input answers for the addition of two
randomly generating integers between 10 and 99 inclusive. The program returns feedback based on the User's answers.

"""

import random
# use code below  to generate a random integer between 30 and 50 for example
print(random.randint(30, 50))

# ********************************** YOUR CODE GOES BELOW HERE *********************************************************
from random import randint
# number of correct answers in row
num_user_answer = []
# total number of correct answers in a row
total_correct_answer = 2

while True:
    try:
        # generates two random numbers
        num1 = randint(10, 99)
        num2 = randint(10, 99)
# calculate the total sum of the two random numbers
        correct_answer = num1 + num2
        # display the addition of the two numbers
        print(f"{num1} + {num2}")
        # this accepts the users answer
        user_answer = int(input("What is your answer: "))
        # validates the user answer
        if user_answer == correct_answer:
            num_user_answer.append(num_user_answer)
            print(f"Correct! You have gotten {len(num_user_answer)} correct in a row")
            if len(num_user_answer) == total_correct_answer + 1:
                print("Congratulations! You mastered addition")
                break

        elif user_answer != correct_answer:
            num_user_answer.clear()
            print(f"incorrect. The correct answer is {correct_answer}")
            # when the user enter an invalid number
    except(TypeError, ValueError):
        print("invalid entry try again")