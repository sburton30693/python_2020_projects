# Spencer Burton
# 1/20/2021
# Class GUI

from tkinter import *


class Application(Frame):
    """A Gui app with three buttons"""

    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.clicks = 0
        self.create_widgets()
    
    def increment(self):
        self.clicks += 1
        self.tclbl = Label(self, text="Total Clicks" + str(self.clicks))

    def create_widgets(self):
        self.tclbl = Label(self, text="Total Clicks")
        self.numclicks = Label(self, text=str(self.clicks))
        self.addbtn = Button(self, text="Add 1", command=self.increment)
        self.subbtn = Button(self, text="Subtract 1")
        self.colbtn = Button(self, text="Change BG Color")

        self.colbtn.grid()
        self.tclbl.grid()
        self.numclicks.grid()
        self.addbtn.grid()
        self.subbtn.grid()

root = Tk()
root.title("Simple Gui")
root.geometry("720x720")
root.configure(bg="#aaaaaa")

app = Application(root)

root.mainloop()
