# Spencer Burton
# 9/29/20
# Number Guessing Game 1.0

import random

# Choose a random number
the_number = random.randint(1, 10)
win = False
count = 0

# Display rules to user
print("\tWelcome to 'Guess My Number'!")
print("I'm thinking of a number between 1 and 10.")
print("Try to guess it in 3 attempts.\n")


# Get user input for guess
user_guess = int(input("Guess a number between 1 and 10: "))

# Check guess against the number
if not win :
    if user_guess == the_number :
        print("Correct!")
        win = True

    elif user_guess > the_number :
        print("Nope, guess lower")

    else :
        print("Nope, guess higher")


# Second Guess

if not win :
    user_guess = int(input("Guess a number between 1 and 10: "))

    if user_guess == the_number :
        print("Correct!")
        win = True

    elif user_guess > the_number :
        print("Nope, guess lower")

    else :
        print("Nope, guess higher")

if not win :
    if count > 0 :
        user_guess = int(input("Guess a number between 1 and 10: "))

        if user_guess == the_number :
            print("Correct!")
            win = True

        elif user_guess > the_number :
            print("Nope, guess lower")

        else :
            print("Nope, guess higher")

if not win :
    if count > 0 :
        user_guess = int(input("Guess a number between 1 and 10: "))

        if user_guess == the_number :
            print("Correct!")
            win = True

        elif user_guess > the_number :
            print("Nope, guess lower")

        else :
            print("Nope, guess higher")


# Third Guess

if not win :
    user_guess = int(input("Guess a number between 1 and 10: "))

    if user_guess == the_number :
        print("Correct!")
        win = True

    elif user_guess > the_number :
        print("Nope, you lost")
        print("The number was", the_number)

    else :
        print("Nope, you lost")
        print("The number was", the_number)


if win :
    print("Great Job")
else :
    print("Better luck next time")
