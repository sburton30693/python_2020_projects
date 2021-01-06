# Spencer Burton
# 1/4/2021
# Re-usable game functions

import sys


def get_yes_no(question):
    """Gets a yes or no response"""
    while True:
        response = input(question)

        if response.lower() in ("y", "yes"):
            return True

        if response.lower() in ("n", "no"):
            return False


def get_integer(question, low, high) :
    """Gets an integer within a range."""
    response = None
    while response not in range(low, high):
        try:
            response = int(input(question))
        except ValueError:
            continue

    return response


def get_float(question, low, high) :
    """Gets a floating point number within a range."""
    response = None
    while response not in range(low, high):
        try:
            response = float(input(question))
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
    def __init__(self, name):
        self.name = name
        self.score = Score()
        self.lives = 3


class Score(object):
    def __init__(self):
        self.value = 0
        self.step_value = 10

    def add_to(self, item_id):
        for i in range(item_id):
            self.value += self.step_value

    def take_from(self, item_id):
        for i in range(item_id):
            self.value += self.step_value

            if self.value < 0:
                self.value = 0


if __name__ == "__main__":
    print("You ran this module directly (and did not 'import' it).")
    input("\nPress enter to exit.")
