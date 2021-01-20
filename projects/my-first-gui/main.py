# Spencer Burton
# 1/20/2021
# Simple GUI

from tkinter import *

root = Tk()
root.title("Simple GUI")
root.geometry("720x720")
# root.resizable(0, 0)
# root.attributes("-fullscreen", True)
# root.attributes("-alpha", 0.75)
root.configure(bg="#aaaaaa")

# Create Frame to place widgets
app = Frame(root)
app["bg"] = "#000000"
app.grid()

# Create Label
lbl = Label(app, text="This is my Label", fg="#000000")
lbl.configure(font=("Courier New", 32))
lbl.grid()

# Create some Buttons
btn = Button(text="Hello There")
btn.configure(height="15")
btn.grid()
btn2 = Button(app)
btn2.config(text="This is another button", font=("Courier New", 32))
btn2.grid()

btn_colors = ["#ff0000", "#00ff00", "#0000ff", "#000000", "#ffffff"]

for i in range(5):
    x = Button(app)
    x["text"] = "Button " + str(i + 1)
    x["bg"] = btn_colors[i]
    x.grid()


app2 = Frame(root)
app2["width"] = 200
app2["height"] = 300
app2["bg"] = "#ff00ff"
app2.grid()

# Kick off the window's event loop
root.mainloop()

# Color Windows
# root = Tk()
# root.title("R")
# root.geometry("720x720")
# root.attributes("-alpha", 0.75)
# root.configure(bg="#ff0000")

# root1 = Tk()
# root1.title("G")
# root1.geometry("720x720")
# root1.attributes("-alpha", 0.75)
# root1.configure(bg="#00ff00")

# root2 = Tk()
# root2.title("B")
# root2.geometry("720x720")
# root2.attributes("-alpha", 0.75)
# root2.configure(bg="#0000ff")
