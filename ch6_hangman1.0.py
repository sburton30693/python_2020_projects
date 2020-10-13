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

index = random.randint(0, len(WORDS) - 1)
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

    while guess == "" or guess[0] in used :
        print("You've already guessed the letter", guess)
        guess = input("\nEnter your guess: ")
        guess = guess.upper()


    used.append(guess[0])
    
    if guess[0] in word :
        print("\nYes!", guess[0], "is in the word!")
    
        # update so_far to include the guess
        new = ""

        for i  in range(len(word)) :
            if guess == word[i] :
                new += guess[0]
            else :
                new += so_far[i]
                
        so_far = new

    else :
        print("\nSorry,", guess[0], "isn't in the word")
        wrong += 1

if wrong == MAX_WRONG :
    print(HANGMAN[wrong])
    print(so_far)
    print("\nYou've been hanged!")
else :
    print(HANGMAN[wrong])
    print(so_far)
    print("\nYou guessed it!")

input("\nPress enter to exit")






























