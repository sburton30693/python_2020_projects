# Spencer Burton
# Starting Template for Tkinter Project

from tkinter import *
from tkinter import filedialog

WIDTH = 200
HEIGHT = 200


class App(Frame):

    def __init__(self, master):
        super(App, self).__init__(master)
        self.create_widgets()

    def create_widgets(self):
        menubar = Menu(self.master)
        self.master.config(menu=menubar)

        file_menu = Menu(menubar)
        file_menu.add_command(label="Open", command=self.on_open)
        menubar.add_cascade(label="File", menu=file_menu)

        self.txt = Text(self)
        self.txt.pack(fill=BOTH, expand=1)

    def on_open(self):
        ftypes = [("Python File", "*.py"), ("All Files", "*")]
        dialog = filedialog.Open(self, filetype=ftypes)
        f1 = dialog.show()

        if f1 != "":
            text = self.read_file(f1)
            self.txt.insert(END, text)

    def read_file(self, filename):
        with open(filename, "r") as f:
            text = f.read()

        return text


def main():
    root = Tk()
    root.geometry(str(WIDTH) + "x" + str(HEIGHT))
    root.title("File Dialog")
    root.resizable(0, 0)

    app = App(root)

    root.mainloop()


main()
