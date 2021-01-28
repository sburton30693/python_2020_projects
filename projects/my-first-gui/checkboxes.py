# Spencer Burton
# 1/28/2021
# Check Boxes

from tkinter import *


class App(Frame):

    def __init__(self, master):
        super(App, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self, text="Choose your favorite food").grid(columnspan=3)
        Label(self, text="Select all that apply:").grid(padx=8, sticky=W)

        self.opt1 = BooleanVar()
        self.opt2 = BooleanVar()
        self.opt3 = BooleanVar()
        Checkbutton(self, text="Pizza",
                    variable=self.opt1, command=self.update).grid(row=2, padx=8, sticky=W)
        Checkbutton(self, text="Tacos",
                    variable=self.opt2, command=self.update).grid(row=3, padx=8, sticky=W)
        Checkbutton(self, text="Hot Dogs",
                    variable=self.opt3, command=self.update).grid(row=4, padx=8, sticky=W)

        self.worst_food = StringVar()
        self.worst_food.set(None)
        Radiobutton(self, text="Yams", value="Yams",
                    variable=self.worst_food, command=self.update).grid(row=5, padx=8, sticky=W)
        Radiobutton(self, text="Food", value="Food",
                    variable=self.worst_food, command=self.update).grid(row=6, padx=8, sticky=W)
        Radiobutton(self, text="Beets", value="Beets",
                    variable=self.worst_food, command=self.update).grid(row=7, padx=8, sticky=W)

        self.output = Text(self, width=35, height=10, wrap=WORD)
        self.output.grid(columnspan=3, padx=8, pady=10)

    def update(self):
        likes = ""
        if self.opt1.get():
            likes += "You like Pizza\n"
        if self.opt2.get():
            likes += "You like Tacos\n"
        if self.opt3.get():
            likes += "You like Hot Dogs\n"

        likes += "Your least favorite food is " + self.worst_food.get()

        self.output.delete(0.0, END)
        self.output.insert(0.0, likes)


def main():
    root = Tk()
    root.title("Check Boxes")
    root.geometry("300x375")
    root.resizable(0, 0)
    app = App(root)

    root.mainloop()


main()
