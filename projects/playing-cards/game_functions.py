# Spencer Burton
# 1/4/2021
# Re-usable game functions

import sys


def ask_yes_no(question):
    """Gets a yes or no response"""
    while True:
        response = input(question)

        if response.lower() in ("y", "yes"):
            return True

        if response.lower() in ("n", "no"):
            return False


def ask_number(question, low, high) :
    """Gets a number within a range."""
    response = None
    while response not in range(low, high):
        try:
            response = int(input(question))
        except ValueError:
            continue

    return response


def open_file(file_path, mode):
    """Open and return an open file with the given permissions"""
    try:
        file = open(file_path, mode)
    except IOError as e:
        print("Unable to open the file", file_path, "Ending program.\n", e)
        input("\nPress enter to exit.")
        sys.exit()
    else:
        return file


class Player(object):
    def __init__(self, name, score=0):
        self.name = name
        self.score = score
        self.lives = 3

if __name__ == "__main__":
    