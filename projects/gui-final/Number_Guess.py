# Ethan Frailey, Spencer Burton, Jordan Jackson
# 2/21
# Guess My Number Game GUI

from tkinter import *
from tkinter import messagebox as mb
import random

# Attributes
HEIGHT = 190  # INT
WIDTH = 550  # INT


def validate_int(number, lower, higher):
    try:
        integer = int(number)

        if number not in range(lower, higher):
            return False

        return True
    except ValueError:
        return False


class App(Frame):
    # Dialogue Lists
    win_list = ["Congrats You won", "DANG!", "Yep That is it", "Sick, you got it correct",
                "Im sorry to tell you this but you got it right"]
    lower_list = ["Sorry but you're too high", "Not quite that high", "Lower it will you", "Become lower"]
    higher_list = ["A little higher buddy", "Your guess is a little too low", "The Number is Higher"]
    lost_list = ["You lost", "Game Over", "You'll get 'em next time", "SNAKE, SNAKE, CAN YOU HEAR ME?"]
    range_lbl_format = "Range 0 - {} | Guesses Remaining: {}"

    def __init__(self, master):
        super(App, self).__init__(master)
        self.grid()
        self.difficulty = 0
        self.range = 10
        self.lower_range = 0
        self.higher_range = 10
        self.number = None
        self.max_guesses = 3
        self.guesses_taken = 0
        self.finished_game = True
        self.diff_text = "Easy"
        self.create_widgets()
        self.set_diff(self.difficulty)

    def create_widgets(self):
        # Create menu bar

        self.menubar = Menu(self.master)
        self.master.config(menu=self.menubar)

        self.game_menu = Menu(self.menubar)

        self.game_menu.add_command(label="New Game", command=self.new_game)
        self.menubar.add_cascade(label="Game", menu=self.game_menu)

        self.diff_menu = Menu(self.menubar)
        self.diff_menu.add_command(label="Easy", command=lambda: self.set_diff(0))
        self.diff_menu.add_command(label="Medium", command=lambda: self.set_diff(1))
        self.diff_menu.add_command(label="Hard", command=lambda: self.set_diff(2))
        self.game_menu.add_cascade(label="Difficulty", menu=self.diff_menu)

        self.game_menu.add_command(label="Exit", command=self.on_exit)
        # Create widgets
        self.title = Label(self, text="Guess My\nNumber", font="Calibra 19 underline")
        self.title.grid(row=0, columnspan=3)

        self.range_label = Label(self, text=str.format("Range 0 - {} | Max Guesses: {}", self.range, self.max_guesses))
        self.range_label.grid(row=1, columnspan=3)

        self.number_entry = Entry(self)
        self.number_entry.grid(row=2, column=1)

        self.lower_label = Label(self, text=("<" + str(self.lower_range)))
        self.lower_label.grid(row=2, column=0, padx=8)

        self.higher_label = Label(self, text=str(self.higher_range))
        self.higher_label.grid(row=2, column=2, padx=8)

        self.output = Text(self, height=10, width=38)
        self.output.config(state=DISABLED)
        self.output.grid(row=0, rowspan=4, column=3, pady=10, padx=10)

        self.submit = Button(self, text="Guess", command=self.guess, width=20)
        self.submit.grid(row=3, columnspan=3)

    def on_exit(self):
        result = mb.askquestion("Exit", "Are you sure you want to exit?")
        if result == "yes":
            sys.exit()
        else:
            pass

    def new_game(self):
        result = None

        if not self.finished_game:
            result = mb.askquestion("New Game",
                                    "You haven't finished the current game. Are you sure you want to start a new one?")

        if result != "yes" and result != None:
            return False

        # Reset everything to default
        self.output.config(state=NORMAL)
        self.output.delete(0.0, END)
        self.output.insert(0.0, str.format("Difficuly: {}\n", self.diff_text))
        self.output.config(state=DISABLED)

        self.finished_game = False
        self.guesses_taken = 0
        self.number = random.randint(0, self.range)

        self.lower_label["text"] = str(self.lower_range) + " <"
        self.higher_label["text"] = "< " + str(self.higher_range)
        self.range_label["text"] = str.format(App.range_lbl_format, self.range, self.max_guesses - self.guesses_taken)
        self.number_entry["text"] = ""

        return True

    def set_diff(self, diff):
        self.difficulty = diff

        if not self.new_game():
            return

        self.output.config(state=NORMAL)
        self.output.delete(0.0, END)

        if diff == 0:
            self.range = 10
            self.lower_range = 0
            self.higher_range = 10
            self.max_guesses = 3

            self.diff_text = "Easy"
            self.output.insert(0.0, "Difficulty: Easy\n")

        elif diff == 1:
            self.range = 50
            self.lower_range = 0
            self.higher_range = 50
            self.max_guesses = 5

            self.diff_text = "Medium"
            self.output.insert(0.0, "Difficulty: Medium\n")

        elif diff == 2:
            self.range = 100
            self.lower_range = 0
            self.higher_range = 100
            self.max_guesses = 10

            self.diff_text = "Hard"
            self.output.insert(0.0, "Difficulty: Hard\n")

        self.output.config(state=DISABLED)

        self.number = random.randint(0, self.range)
        print("num:",self.number)

        self.lower_label["text"] = str(self.lower_range) + " <"
        self.higher_label["text"] = "< " + str(self.higher_range)
        self.range_label["text"] = str.format(App.range_lbl_format, self.range, self.max_guesses - self.guesses_taken)

    def guess(self):
        if self.finished_game:
            return

        try:
            int(self.number_entry.get())
        except ValueError:
            return

        if self.guesses_taken >= self.max_guesses:
            self.output.config(state=NORMAL)

            self.output.delete(0.0, END)
            self.output.insert(END, random.choice(App.lost_list) + "\n\nGAME OVER")
            self.finished_game = True

            self.output.config(state=DISABLED)

        else:
            self.guesses_taken += 1
            self.range_label["text"] = str.format(App.range_lbl_format, self.range, self.max_guesses - self.guesses_taken)

            # Check again
            if self.guesses_taken >= self.max_guesses:
                self.output.config(state=NORMAL)

                self.output.delete(0.0, END)
                self.output.insert(END, random.choice(App.lost_list) + "\n\nGAME OVER")
                self.finished_game = True

                self.output.config(state=DISABLED)

            else:
                int_guess = int(self.number_entry.get())

                self.output.config(state=NORMAL)
                self.output.insert(END, str.format("Guess #{} : {}\n", self.guesses_taken, int_guess))

                if int_guess > self.number:
                    self.output.config(state=NORMAL)
                    self.output.insert(END, random.choice(App.lower_list) + "\n")
                    self.output.config(state=DISABLED)

                elif int_guess < self.number:
                    self.output.config(state=NORMAL)
                    self.output.insert(END, random.choice(App.higher_list) + "\n")
                    self.output.config(state=DISABLED)

                elif int_guess == self.number:
                    self.output.config(state=NORMAL)

                    self.output.delete(0.0, END)
                    self.output.insert(END, random.choice(App.win_list) + "\n\nYOU WON!")
                    self.finished_game = True

                    self.output.config(state=DISABLED)

        self.output.see(END)


def launch():
    root = Tk()
    root.title("Guess My Number")
    root.geometry(str(WIDTH) + "x" + str(HEIGHT))
    root.resizable(0, 0)
    app = App(root)

    root.mainloop()


launch()
