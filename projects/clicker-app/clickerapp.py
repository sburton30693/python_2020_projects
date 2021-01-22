# Spencer Burton
# 1/22/2021
# Clicker Program Gui / Using Event Handlers

from tkinter import *


class App(Frame):
    """GUI application which counts button clicks."""

    def __init__(self, master):
        super(App, self).__init__(master)
        self.grid()
        self.total = 0
        self.colors = ["White", "Pink", "Red", "Yellow", "Orange", "Green", "Blue", "Purple", "Dark Blue", "Black", "Grey"]
        self.color_index = 0
        self.create_widgets()

    def create_widgets(self):
        # Create widgets
        self.lbl1 = Label(self, text="Total Clicks:")
        self.lbl2 = Label(self, text=str(self.total))
        self.add_btn = Button(self, text=" + ")
        self.add_btn["command"] = self.add_to_counter
        self.min_btn = Button(self, text=" - ")
        self.min_btn["command"] = self.min_from_counter
        self.col_btn = Button(self, text="Change Color", width=28)
        self.col_btn["command"] = self.change_color

        # Add widgets to grid
        self.col_btn.grid()
        self.lbl1.grid()
        self.lbl2.grid()
        self.add_btn.grid()
        self.min_btn.grid()

    def add_to_counter(self):
        self.total += 1
        self.lbl2.config(text=str(self.total))
        self.change_label_bg()

    def min_from_counter(self):
        self.total -= 1

        # Make sure total is not negative
        if self.total < 0:
            self.total = 0

        self.lbl2.config(text=str(self.total))
        self.change_label_bg()

    def change_color(self):
        # Increment the counter
        self.color_index = (self.color_index + 1) % len(self.colors)

        # Change most of the backgrounds
        self["bg"] = self.colors[self.color_index]
        self.master["bg"] = self.colors[self.color_index]
        self.lbl1["bg"] = self.colors[self.color_index]

        # Change the text color of the labels if the background is too dark
        if self.colors[self.color_index] == "Black" or self.colors[self.color_index] == "Dark Blue" :
            self.lbl1["fg"] = "White"
        else:
            self.lbl1["fg"] = "Black"

    def change_label_bg(self):
        # Cycles of 1000
        count = self.total % 1000
        color_format = "#{:02x}{:02x}{:02x}"

        # These are some equations I made on Desmos graphing calculator
        # They're specially designed to not go above 255
        r = -count * (count - 2000) * 0.000255
        g = max(-(count + 30) * (count - 200) * 0.019, 0)
        b = max(-(count - 100) * (count - 250) * 0.03, 0)

        color_string = str.format(color_format, int(r), int(g), int(b))
        self.lbl2["bg"] = color_string

    
def main():
    # Create Root Window
    root = Tk()
    root.title("Counter")
    root.geometry("205x240")
    root.resizable(0, 0)
    app = App(root)

    # Kick off window's main event loop
    root.mainloop()


main()
