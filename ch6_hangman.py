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
--------
""",
"""

 ____
|    |
|    Q
|
|
|
|
--------
""",
"""

 ____
|    |
|    Q
|    |
|    |
|
|
--------
""",
"""

 ____
|    |
|    Q
|   /|
|    |
|
|
--------
""",
"""

 ____
|    |
|    Q
|   /|\\
|    |
|
|
--------
""",
"""

 ____
|    |
|    Q
|   /|\\
|    |
|   /
|
--------
""",
"""

 ____
|    |
|    Q
|   /|\\
|    |
|   / \\
|
--------
"""
)

MAX_WRONG = len(HANGMAN) - 1
WORDS = ("TUPLE", "LIST", "LOOP", "KEYWORD", "LOGICAL",
         "OPERATOR", "BOOLEAN", "FLOAT", "INTEGER")

word = random.choice(WORDS) # Word to be guessed
so_far = "_ " * len(word) # Placeholders for letters in the word
used = [] # Letters already guessed
wrong = 0 # Number of wrong guesses

print("Welcome to Hangman. Good luck!\n")
print(HANGMAN[0])
print(so_far)


