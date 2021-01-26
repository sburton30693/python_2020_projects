# Spencer Burton
# 1/26/20
# Demonstrates Text and Entry widgets, and the Grid Layout Manager

from tkinter import *


class App(Frame):
    usernames = ["sburton52"]
    passwords = ["Password"]
    tries = 0

    def __init__(self, master):
        super(App, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.lbl = Label(self, text="Enter your credentials to gain entry")
        self.lbl.grid(columnspan=3)
        self.user_lbl = Label(self, text="Username:")
        self.user_lbl.grid(sticky=E)
        self.user_text = Entry(self, width=30)
        self.user_text.grid(column=1, row=1, sticky=W)
        self.pass_lbl = Label(self, text="Password:")
        self.pass_lbl.grid(sticky=E)
        self.pass_text = Entry(self, width=30)
        self.pass_text.grid(column=1, row=2, sticky=W)
        self.btn = Button(self, text="Log In", command=self.submit)
        self.btn.grid(sticky=E)
        self.btn1 = Button(self, text="Sign Up", command=self.add_user)
        self.btn1.grid(sticky=W, column=1, row=3)
        self.output = Text(self, width=53)
        self.output.grid(columnspan=3)

    def submit(self):
        username = self.user_text.get()
        password = self.pass_text.get()

        if self.tries > 3:
            message = "Too many failed attempts, contacting local authorities..."
        else:
            for i in range(len(self.usernames)):
                if username.lower() == self.usernames[i]:
                    if password == self.passwords[i]:
                        message = "You got in "
                        self.tries = 0
                        break
                    else:
                        message = "Invalid Password"
                        self.tries += 1
                else:
                    message = "Invalid Username"
                    self.tries += 1

        # Check again
        if self.tries > 3:
            message = "Too many failed attempts, contacting local authorities..."

        self.output.delete(0.0, END)
        self.output.insert(0.0, message)

    def add_user(self):
        if self.tries > 3:
            return

        username = self.user_text.get()
        password = self.pass_text.get()

        if username == "" or password == "":
            message = "Username and password cannot be empty"
        elif username.lower() in self.usernames:
            message = "That username is already taken"
        else:
            self.usernames.append(username.lower())
            self.passwords.append(password)
            message = "Sign up successful"

        self.output.delete(0.0, END)
        self.output.insert(0.0, message)


def main():
    root = Tk()
    root.title("Text Boxes")
    root.geometry("425x400")

    app = App(root)

    root.mainloop()


main()
