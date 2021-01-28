# Spencer Burton
# 1/28/2021
# Pizza Orgering Gui

from tkinter import *


class App(Frame):

    def __init__(self, master):
        super(App, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self, text="Welcome to GUI Pizza Online Order").grid(columnspan=3)
        Label(self, text="Recipient Credentials:").grid(columnspan=3, pady=5)

        Label(self, text="Name:").grid(column=0, sticky=E)
        self.name = Entry(self, width=24)
        self.name.grid(row=2, column=1)
        Label(self, text="Address:").grid(column=0, sticky=E)
        self.addr = Entry(self, width=24)
        self.addr.grid(row=3, column=1)
        Label(self, text="Phone Number:").grid(column=0, sticky=E)
        self.phone = Entry(self, width=24)
        self.phone.grid(row=4, column=1)

        Label(self, text="Pizza Order:").grid(columnspan=3, pady=5)

        Label(self, text="Size:").grid(padx=8, sticky=W)
        self.pizza_size = StringVar()
        self.pizza_size.set("Small")
        Radiobutton(self, text="Small", value="Small",
                    variable=self.pizza_size).grid(row=7, column=0)
        Radiobutton(self, text="Medium", value="Medium",
                    variable=self.pizza_size).grid(row=7, column=1)
        Radiobutton(self, text="Large", value="Large",
                    variable=self.pizza_size).grid(row=7, column=2)

        Label(self, text="Toppings:").grid(padx=8, sticky=W)
        TOPPINGS = ("Pepperoni", "Jalapeno", "Olive", "Mushroom", "Bell Pepper", "Chicken",
                    "Pineapple", "Extra Cheese", "Onions", "Sausage", "Spinach", "Anchovies")
        self.boolean_vars = []
        for i in range(len(TOPPINGS)):
            row = 9 + i // 2
            column = i % 2
            pad = 8
            if column == 1:
                pad = 0

            self.boolean_vars.append(BooleanVar())
            Checkbutton(self, text=TOPPINGS[i],
                        variable=self.boolean_vars[i]
                        ).grid(row=row, column=column, padx=pad, sticky=W)

        self.output = Text(self, width=35, height=10)
        self.output.grid(columnspan=3, padx=16, pady=8)


def main():
    root = Tk()
    root.title("GUI Pizza")
    root.geometry("320x600")
    root.resizable(0, 0)
    app = App(root)

    root.mainloop()


main()
