# Spencer Burton, Ethan Fraily, Jordan Jackson

from tkinter import *

WIDTH = 180
HEIGHT = 200


class App(Frame):

    def __init__(self, master):
        super(App, self).__init__(master)
        self.grid()
        self.first_number = ""
        self.second_number = ""
        self.operation = ""
        self.result = ""
        self.create_widgets()

    def create_widgets(self):
        # Create the persistent widgets
        self.output = Text(self, height=2, width=20, state=DISABLED)
        self.output.tag_configure("right", justify="right")

        # Grid all the widgets
        Label(self, text="Calculator").grid(row=0, columnspan=4)
        self.output.grid(row=1, columnspan=4, padx=8)

        # Number buttons
        Button(self, width=3, text="1", command=lambda: self.pressed("1")).grid(row=3, column=0)
        Button(self, width=3, text="2", command=lambda: self.pressed("2")).grid(row=3, column=1)
        Button(self, width=3, text="3", command=lambda: self.pressed("3")).grid(row=3, column=2)
        Button(self, width=3, text="4", command=lambda: self.pressed("4")).grid(row=4, column=0)
        Button(self, width=3, text="5", command=lambda: self.pressed("5")).grid(row=4, column=1)
        Button(self, width=3, text="6", command=lambda: self.pressed("6")).grid(row=4, column=2)
        Button(self, width=3, text="7", command=lambda: self.pressed("7")).grid(row=5, column=0)
        Button(self, width=3, text="8", command=lambda: self.pressed("8")).grid(row=5, column=1)
        Button(self, width=3, text="9", command=lambda: self.pressed("9")).grid(row=5, column=2)
        Button(self, width=3, text="0", command=lambda: self.pressed("0")).grid(row=6, column=1)
        Button(self, width=3, text=".", command=lambda: self.pressed(".")).grid(row=6, column=2)

        # Operation buttons
        Button(self, width=4, text="+", command=lambda: self.pressed("+")).grid(row=2, column=3)
        Button(self, width=4, text="-", command=lambda: self.pressed("-")).grid(row=3, column=3)
        Button(self, width=4, text="*", command=lambda: self.pressed("*")).grid(row=4, column=3)
        Button(self, width=4, text="/", command=lambda: self.pressed("/")).grid(row=5, column=3)

        # Equal Button
        Button(self, width=4, text="=", command=lambda: self.pressed("=")).grid(row=6, column=3)

        # Clear Button
        Button(self, width=14, text="Clear", command=self.clear).grid(row=2, columnspan=3)

    def pressed(self, button):
        # Check if the result has been done
        if self.result != "" and button in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."):
            self.clear()

        # Check for answer button
        if button in ("+", "-", "*", "/") and self.result != "" and self.result != "Divide by Zero":
            old_result = self.result
            self.clear()
            self.first_number = old_result

            if button in ("+", "-", "*", "/"):
                self.operation = button

        # Add digits to first number
        elif button in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".") and self.operation == "":
            if button == "." and "." in self.first_number:
                pass
            else:
                self.first_number += button
        elif self.first_number != "" and self.operation == "" and button != "=":
            self.operation = button
        elif button in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."):
            if button == "." and "." in self.second_number:
                pass
            else:
                self.second_number += button

        # Check for equals
        if button == "=":
            got_result = self.equal()

        # Print stuff
        self.output.config(state=NORMAL)
        self.output.delete(0.0, END)
        self.output.insert(END, str.format("{} {} {}\n", self.first_number, self.operation, self.second_number), "right")
        self.output.insert(END, self.result, "right")
        self.output.config(state=DISABLED)

    def equal(self):
        if self.operation != "" and self.second_number != "":
            num1 = float(self.first_number)
            num2 = float(self.second_number)

            if self.operation == "+":
                self.addition(num1, num2)
            elif self.operation == "-":
                self.subtraction(num1, num2)

            elif self.operation == "*":
                self.multiply(num1, num2)

            elif self.operation == "/":
                self.division(num1, num2)
        else:
            return False

        return True

    def clear(self):
        self.output.config(state=NORMAL)
        self.output.delete(0.0, END)
        self.output.config(state=DISABLED)

        # Clear variables
        self.first_number = ""
        self.second_number = ""
        self.operation = ""
        self.result = ""

    def addition(self, num1, num2):
        self.result = str(num1 + num2)

    def subtraction(self, num1, num2):
        self.result = str(num1 - num2)

    def multiply(self, num1, num2):
        self.result = str(num1 * num2)

    def division(self, num1, num2):
        try:
            self.result = str(num1 / num2)
        except:
            self.result = "Divide by Zero"


def main():
    root = Tk()
    root.geometry(str(WIDTH) + "x" + str(HEIGHT))
    root.title("Calculator")
    root.resizable(0, 0)
    root.attributes('-toolwindow', True)

    app = App(root)

    root.mainloop()


main()
