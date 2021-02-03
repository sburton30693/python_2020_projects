# Spencer Burton
# 2/3/2021
# Layout Managers in Tkinter

from tkinter import *
from PIL import Image, ImageTk

WIDTH = 250
HEIGHT = 750


class App(Frame):

    def __init__(self, master):
        super(App, self).__init__(master)
        self.pack(fill=BOTH, expand=1)
        self.create_widgets()

    def create_widgets(self):
        self.config(bg="Dark Grey")

        Label(self, text="My favorite Images", width=20).place(x=WIDTH / 2 - 70, y=5)

        # Load in Images
        img1 = Image.open("spaghetti.jpg")
        img2 = Image.open("prism.jpg")
        img3 = Image.open("pyramids.jpg")

        # Converting images to tk objects
        pic1 = ImageTk.PhotoImage(img1)
        pic2 = ImageTk.PhotoImage(img2)
        pic3 = ImageTk.PhotoImage(img3)

        self.img_lbl1 = Label(self, image=pic1)
        self.img_lbl1.image = pic1
        self.img_lbl1.place(x=12.5, y=50)
        self.img_lbl2 = Label(self, image=pic2)
        self.img_lbl2.image = pic2
        self.img_lbl2.place(x=22, y=230)
        self.img_lbl3 = Label(self, image=pic3)
        self.img_lbl3.image = pic3
        self.img_lbl3.place(x=22, y=450)


def main():
    root = Tk()
    root.geometry(str(WIDTH) + "x" + str(HEIGHT))
    root.title("Layout Managers")
    root.resizable(0, 0)

    app = App(root)

    root.mainloop()


main()
