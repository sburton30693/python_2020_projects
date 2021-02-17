# Spencer Burton
# Starting Template for Tkinter Project

from tkinter import *
from tkinter import colorchooser as cc

WIDTH = 400
HEIGHT = 220


class App(Frame):

    def __init__(self, master):
        super(App, self).__init__(master)
        self.pack(fill=BOTH, expand=1)
        self.create_widgets()

    def create_widgets(self):
        self.btn = Button(self, text="Choose Color", command=self.on_choose)
        self.btn.place(x=30, y=30)

        self.frame = Frame(self, border=1, relief=SUNKEN, width=100, height=100)
        self.frame.place(x=160, y=30)

    def on_choose(self):
        (rgb, hx) = cc.askcolor()
        self.frame.config(bg=hx)


def main():
    root = Tk()
    root.geometry(str(WIDTH) + "x" + str(HEIGHT))
    root.title("Color Picker")
    root.resizable(0, 0)

    app = App(root)

    root.mainloop()


main()
