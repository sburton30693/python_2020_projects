# Spencer Burton
# 10/9/2020
# Hangman Game

import random

HANGMAN = (
"""
 ____ 
|    |
|
|
|
|
|
|_______
""",
"""
 ____
|    |
|    Q
|
|
|
|
|_______
""",
"""
 ____
|    |
|    Q
|    |
|    |
|
|
|_______
""",
"""
 ____
|    |
|    Q
|   /|
|    |
|
|
|_______
""",
"""
 ____
|    |
|    Q
|   /|\\
|    |
|
|
|_______
""",
"""
 ____
|    |
|    Q
|   /|\\
|    |
|   /
|
|_______
""",
"""
 ____
|    |
|    Q
|   /|\\
|    |
|   / \\
|
|_______
"""
)

MAX_WRONG = len(HANGMAN) - 1
WORDS = ("TUPLE", "LIST", "LOOP", "KEYWORD", "LOGICAL", "OPERATOR", "BOOLEAN", "FLOAT", "INTEGER")
DEFINITIONS = ("A variable that contains multiple variables that can't be modified",
               "A variable that contains multiple variables that can be changed or have more added",
               "Can be a for or while loop that run over the same lines of code based on a condition",
               "A word that is reserved by Python and can't be used as a variable name",
               "A type of expression using comparison operators and booleans to control decisions",
               "A symbol that does some mathematical or logical operation on some variables",
               "A data type that stores either true or false",
               "A data type that stores a decimal number",
               "A data type that stores a positive or negative whole number")

index = random.randint(0, len(WORDS) - 1) # Index of the chosen word(Also used for definitions)
word = WORDS[index] # Word to be guessed
so_far = "-" * len(word) # Placeholders for letters in the word
used = [] # Letters already guessed
wrong = 0 # Number of wrong guesses

print("Welcome to Hangman. Good luck!\n")

while wrong < MAX_WRONG and so_far != word:
    print(HANGMAN[wrong])
    print(so_far)
    print("\nYou've used the following letters:\n" + str(used))

    guess = input("\nEnter your guess: ")
    guess = guess.upper()

    while guess == "" or guess in used :
        print("You've already guessed the letter", guess)
        guess = input("\nEnter your guess: ")
        guess = guess.upper()

    used.append(guess)

    # If the user guesses the word it's an automatic win
    if guess == word :
        so_far = guess
        break
    
    if guess in word :
        print("\nYes!", guess, "is in the word!")
    
        # update so_far to include the guess
        new = ""

        for i  in range(len(word)) :
            if guess == word[i] :
                new += guess
            else :
                new += so_far[i]
                
        so_far = new

    else :
        print("\nSorry,", guess, "isn't in the word")
        wrong += 1

# Final win or loss information
if wrong == MAX_WRONG :
    print(HANGMAN[wrong])
    print(so_far)
    print("\nYou've been hanged!")
else :
    print(HANGMAN[wrong])
    print(so_far)
    print("\nYou guessed it!")
    print("\nHere's the definition:")
    print(DEFINITIONS[index])

input("\nPress enter to exit")
