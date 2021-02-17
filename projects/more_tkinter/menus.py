from tkinter import *
import os


HEIGHT = 200
WIDTH = 200
TITLE = "new program"
BACKGROUND = "darkgray"
FONT = "San_Serif"


class App(Frame):
    def __init__(self, master):
        super(App, self).__init__(master)
        self.col = 0
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        menubar = Menu(self.master)
        self.master.config(menu=menubar)
        file_menu = Menu(menubar)
        file_menu.add_command(label="Exit", command=self.on_exit)
        file_menu.add_command(label="Open", command=self.on_open)
        file_menu.add_command(label="Save", command=self.on_save)
        menubar.add_cascade(label="File", menu=file_menu)

        edit_menu = Menu(menubar)
        edit_menu.add_command(label="Create Frame", command=self.create_frame)
        edit_menu.add_command(label="Destroy Frame", command=self.destroy_frame)
        menubar.add_cascade(label="Edit", menu=edit_menu)

        sub_menu = Menu(file_menu)
        sub_menu.add_command(label="New feed")
        sub_menu.add_command(label="Bookmarks")
        sub_menu.add_command(label="Mail")

        file_menu.add_separator()
        file_menu.add_cascade(label="import", menu=sub_menu)

    def on_exit(self):
        self.quit()
        
    def on_open(self):
        os.system("more_widgets.py")
        
    def on_save(self):
        os.system("explorer.exe")
        
    def create_frame(self):
        self.frame1 = Frame(self, bg="red", width=250, height=250)
        self.frame1.grid(row=1, column=self.col)
        self.lbl1 = Label(self.frame1, text="testing")
        self.lbl1.pack(padx=20, pady=20, fill=BOTH, expand=1)
        self.lbl1["text"] = "change"
        
        self.col += 1

    def destroy_frame(self):
        self.frame1.destroy()


def main():
    root = Tk()
    root.geometry(str.format("{}x{}", WIDTH, HEIGHT))
    root.title(TITLE)
    root.config(bg=BACKGROUND)
    app = App(root)
    root.mainloop()


main()
