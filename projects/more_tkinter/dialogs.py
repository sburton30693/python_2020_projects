# Spencer Burton
# Starting Template for Tkinter Project

from tkinter import *
from tkinter import messagebox as mb

WIDTH = 200
HEIGHT = 200


class App(Frame):

    def __init__(self, master):
        super(App, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        error = Button(self, text="Error", command=self.on_error)
        error.grid(padx=4, pady=5)
        warning = Button(self, text="Warning", command=self.on_warn)
        warning.grid(row=1, column=0)
        question = Button(self, text="Question", command=self.on_quest)
        question.grid(row=0, column=1)
        inform = Button(self, text="Information", command=self.on_info)
        inform.grid(row=1, column=1)

    def on_error(self):
        mb.showerror("Error", "Could not open file")

    def on_warn(self):
        mb.showwarning("Warning", "Deprecated function call")

    def on_quest(self):
        if mb.askquestion("Question", "Are you sure you want to quit?") == "yes":
            self.quit()

    def on_info(self):
        mb.showinfo("Info", "Download completed")


def main():
    root = Tk()
    root.geometry(str(WIDTH) + "x" + str(HEIGHT))
    root.title("Message Box Dialogs")
    root.resizable(0, 0)

    app = App(root)

    root.mainloop()


main()
