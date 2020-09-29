# Spencer Burton
# 9/29/20
# Number Guessing Game 1.0

import random

# Choose a random number
the_number = random.randint(1, 10)

# Display rules to user
print("\tWelcome to 'Guess My Number'!")
print("I'm thinking of a number between 1 and 10.")
print("Try to guess it in 3 attempts.\n")

# Get user input for guess
user_guess = int(input("Guess a number between 1 and 10: "))

# Check guess against the number
if user_guess == the_number :
    pass

elif user_guess > the_number :
    pass
    print("Nope, try guessing lower")

else :
    pass
    print("Nope, try guessing higher")
