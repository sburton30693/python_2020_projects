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
        Label(self, text="Welcome to GUI Pizza Online Order", font="Calibra 13").grid(columnspan=3)
        Label(self, text="Recipient Credentials:", font="Calibra 11 bold").grid(columnspan=3, pady=5)

        Label(self, text="Name:").grid(column=0, sticky=E)
        self.name = Entry(self, width=24)
        self.name.grid(row=2, column=1, columnspan=2)
        Label(self, text="Address:").grid(column=0, sticky=E)
        self.addr = Entry(self, width=24)
        self.addr.grid(row=3, column=1, columnspan=2)
        Label(self, text="Phone Number:").grid(column=0, sticky=E)
        self.phone = Entry(self, width=24)
        self.phone.grid(row=4, column=1, columnspan=2)

        Label(self, text="Pizza Order:", font="Calibra 11 bold").grid(columnspan=3, pady=5)

        # Pizza Size
        Label(self, text="Size:", font="Calibra 10 bold").grid(padx=8, sticky=W)
        self.pizza_size = StringVar()
        self.pizza_size.set("Small")
        Radiobutton(self, text="Small", value="Small",
                    variable=self.pizza_size).grid(row=7, column=0, padx=8, sticky=W)
        Radiobutton(self, text="Medium", value="Medium",
                    variable=self.pizza_size).grid(row=7, column=1, sticky=W)
        Radiobutton(self, text="Large", value="Large",
                    variable=self.pizza_size).grid(row=7, column=2, sticky=W)

        # Crust
        Label(self, text="Crust:", font="Calibra 10 bold").grid(padx=8, sticky=W)
        self.pizza_crust = StringVar()
        self.pizza_crust.set("Classic")
        Radiobutton(self, text="Classic", value="Classic",
                    variable=self.pizza_crust).grid(row=9, column=0, padx=8, sticky=W)
        Radiobutton(self, text="Thin", value="Thin",
                    variable=self.pizza_crust).grid(row=9, column=1, sticky=W)
        Radiobutton(self, text="Stuffed", value="Stuffed",
                    variable=self.pizza_crust).grid(row=9, column=2, sticky=W)
        Radiobutton(self, text="Deep Dish", value="Deep Dish",
                    variable=self.pizza_crust).grid(row=10, column=0, padx=8, sticky=W)
        Radiobutton(self, text="Garlic", value="Garlic",
                    variable=self.pizza_crust).grid(row=10, column=1, sticky=W)
        Radiobutton(self, text="Neopolitan", value="Neopolitan",
                    variable=self.pizza_crust).grid(row=10, column=2, sticky=W)

        Label(self, text="Toppings:", font="Calibra 10 bold").grid(padx=8, sticky=W)
        self.TOPPINGS = ("Pepperoni", "Jalapeno", "Olive", "Mushroom", "Bell Pepper", "Chicken",
                         "Pineapple", "Extra Cheese", "Onions", "Sausage", "Spinach", "Anchovies")
        self.topping_vars = []

        for i in range(len(self.TOPPINGS)):
            row = 12 + i // 3
            column = i % 3
            pad = 8

            if column != 0:
                pad = 0

            self.topping_vars.append(BooleanVar())
            Checkbutton(self, text=self.TOPPINGS[i], variable=self.topping_vars[i]
                        ).grid(row=row, column=column, padx=pad, sticky=W)

        Button(self, text="Submit Order", command=self.submit).grid(columnspan=3, pady=6)
        self.output = Text(self, wrap=WORD, width=38, height=10)
        self.output.grid(columnspan=3, padx=16, pady=8)

    def submit(self):
        order = "Order Submitted:\n"
        price = 0.0

        # Add credentials to order string
        order += str.format("Name    : {}\nAddress : {}\nPhone # : {}\n", self.name.get(), self.addr.get(), self.phone.get())

        # Add Size and Crust
        order += str.format("Size: {:7} Crust: {}\n", self.pizza_size.get(), self.pizza_crust.get())

        if self.pizza_size.get() == "Small":
            price += 8.0
        elif self.pizza_size.get() == "Medium":
            price += 10.0
        elif self.pizza_size.get() == "Large":
            price += 12.0

        if self.pizza_crust.get() != "Classic":
            price += 1.50

        # Add toppings
        order += "Toppings: "

        for i in range(len(self.TOPPINGS)):
            if self.topping_vars[i].get():
                order += str.format("{}, ", self.TOPPINGS[i])
                price += 0.50

        # Calculate Tax and add Price to order string
        price += price * 0.05

        order += str.format("\nPrice: ${:.2f}", price)

        self.output.delete(1.0, END)
        self.output.insert(1.0, order)


def main():
    root = Tk()
    root.title("GUI Pizza")
    root.geometry("340x625")
    root.resizable(0, 0)
    app = App(root)

    root.mainloop()


main()
