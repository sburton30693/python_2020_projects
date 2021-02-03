# Spencer Burton
# Starting Template for Tkinter Project

from tkinter import *

WIDTH = 720
HEIGHT = 440


class App(Frame):

    def __init__(self, master):
        super(App, self).__init__(master)
        self.create_widgets()

    def create_widgets(self):
        pass


def main():
    root = Tk()
    root.geometry(str(WIDTH) + "x" + str(HEIGHT))
    root.title("Tkinter Template")
    root.resizable(0, 0)

    app = App(root)

    root.mainloop()


main()
