# Spencer Burton
# 9/29/20
# Number Guessing Game 1.1

import random

# Setting Variables
max_number = 10
num_trys = 3
diff = 1 

win = False

# Display rules to user
print("Welcome to 'Guess My Number'!")

# Difficulty Setting
question = input("What difficulty would you like Easy, Medium, or Hard? ")

if question.startswith("e") or question.startswith("E") :
    max_number = 10
    num_trys = 3
    diff = 1 
elif question.startswith("m") or question.startswith("M") :
    max_number = 50
    num_trys = 5
    diff = 2
else :
    max_number = 100
    num_trys = 10
    diff = 3 

# Generate Random Number
the_number = random.randint(1, max_number)

print(str.format("I'm thinking of a number between 1 and {}.", max_number))
print(str.format("Try to guess it in {} attempts.\n", num_trys))


# First Guess
user_guess = int(input("Guess a number between 1 and " + str(max_number) + ": "))

if user_guess == the_number :
    win = True

elif user_guess > the_number :
    print("Nope, guess lower")

else :
    print("Nope, guess higher")


# Second Guess
if not win :
    user_guess = int(input("Guess a number between 1 and " + str(max_number) + ": "))

    if user_guess == the_number :
        win = True

    elif user_guess > the_number :
        print("Nope, guess lower")

    else :
        print("Nope, guess higher")

        
# Extra Guesses for higher difficulty

# 3
if not win and diff > 1 :
    user_guess = int(input("Guess a number between 1 and " + str(max_number) + ": "))

    if user_guess == the_number :
        win = True

    elif user_guess > the_number :
        print("Nope, guess lower")

    else :
        print("Nope, guess higher")

# 4
if not win and diff > 1 :
    user_guess = int(input("Guess a number between 1 and " + str(max_number) + ": "))

    if user_guess == the_number :
        win = True

    elif user_guess > the_number :
        print("Nope, guess lower")

    else :
        print("Nope, guess higher")

# 5
if not win and diff > 2 :
    user_guess = int(input("Guess a number between 1 and " + str(max_number) + ": "))

    if user_guess == the_number :
        win = True

    elif user_guess > the_number :
        print("Nope, guess lower")

    else :
        print("Nope, guess higher")

 # 6
if not win and diff > 2 :
    user_guess = int(input("Guess a number between 1 and " + str(max_number) + ": "))

    if user_guess == the_number :
        win = True

    elif user_guess > the_number :
        print("Nope, guess lower")

    else :
        print("Nope, guess higher")

# 7
if not win and diff > 2 :
    user_guess = int(input("Guess a number between 1 and " + str(max_number) + ": "))

    if user_guess == the_number :
        win = True

    elif user_guess > the_number :
        print("Nope, guess lower")

    else :
        print("Nope, guess higher")

# 8
if not win and diff > 2 :
    user_guess = int(input("Guess a number between 1 and " + str(max_number) + ": "))

    if user_guess == the_number :
        win = True

    elif user_guess > the_number :
        print("Nope, guess lower")

    else :
        print("Nope, guess higher")

# 9
if not win and diff > 2 :
    user_guess = int(input("Guess a number between 1 and " + str(max_number) + ": "))

    if user_guess == the_number :
        win = True

    elif user_guess > the_number :
        print("Nope, guess lower")

    else :
        print("Nope, guess higher")
        

# Final Guess
if not win :
    user_guess = int(input("Guess a number between 1 and " + str(max_number) + ": "))

    if user_guess == the_number :
        win = True


if win :
    print("Correct!")
else :
    print("Nope, you lost")
    
print("The number was", the_number)
