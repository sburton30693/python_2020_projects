# Spencer Burton
# Starting Template for Tkinter Project

from tkinter import *
from tkinter.ttk import *

WIDTH = 720
HEIGHT = 440


class App(Frame):

    def __init__(self, master):
        super(App, self).__init__(master)
        self.pack(fill=X)
        self.create_widgets()

    def create_widgets(self):
        self.items_list = [1, 2, 3, 4, 5, "hello"]
        self.combo_box = Combobox(self, values=self.items_list)

        # Set the default value
        self.combo_box.current(0)
        self.combo_box.pack(side=LEFT)

        self.list_box = Listbox(self)
        list_items = ["test1", "test2", "test3", "test4", "test5"]
        for i in range(len(list_items)):
            self.list_box.insert(i, list_items[i])
        self.list_box.pack(side=LEFT)

        self.progress_bar = Progressbar(self, length=200, value=50)
        self.progress_bar.pack(side=LEFT)

        self.increase = Button(self, text=">>>>>>", command=self.inc)
        self.increase.pack(side=LEFT)
        self.decrease = Button(self, text="<<<<<<", command=self.dec)
        self.decrease.pack(side=LEFT)
    
        self.submit = Button(self, text="Try me", command=self.on_change_values)
        self.submit.pack(side=LEFT)


    def inc(self):
        self.progress_bar["value"] = self.progress_bar["value"] + 1

    def dec(self):
        self.progress_bar["value"] = self.progress_bar["value"] - 1

    def on_change_values(self):
        cdtext = self.combo_box.get()
        print(cdtext)
        self.list_box.insert(END, cdtext)
        lbtext = self.list_box.get(ANCHOR)
        print(lbtext)
        self.items_list.append(lbtext)
        self.combo_box["values"] = self.items_list;
        


def main():
    root = Tk()
    #root.geometry(str.format("{}x{}", WIDTH, HEIGHT))
    root.title("Tkinter Template")
    root.resizable(0, 0)

    app = App(root)

    root.mainloop()


main()
