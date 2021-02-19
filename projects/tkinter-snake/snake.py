# Spencer Burton
# 2/19/2021
# Snake Game in tkinter

import random
import sys
from tkinter import *
from PIL import ImageTk, Image


class Cons:
    BOARD_WIDTH  = 300
    BOARD_HEIGHT = 300
    DELAY = 100
    DOT_SIZE = 10
    MAX_RAND_POS = 27


class Board(Canvas):

    def __init__(self):
        super(Board, self).__init__(width=Cons.BOARD_WIDTH, height=Cons.BOARD_HEIGHT, background="black", highlightthickness=0)
        self.init_game()
        self.pack()

    def init_game(self):
        """Initializes the game"""
        self.in_game = True
        self.dots = 3
        self.score = 0

        # Variables used to move snake object
        self.move_x = Cons.DOT_SIZE
        self.move_y = 0

        # Starting apple coordinates
        self.apple_x = 100
        self.apple_y = 190

        # Load images
        self.load_images()

        # Create Game Objects
        self.create_objects()

        # Place an apple on the screen
        self.locate_apple()
        self.bind_all("<Key>", self.on_key_press)
        self.after(Cons.DELAY, self.on_timer)

    def on_timer(self):
        """Creates a game cycle each timer event"""
        self.draw_score()
        self.check_collision()
        
        if self.in_game():
            self.check_apple_collision()
            self.move_snake()
            self.after(Cons.DELAY, self.on_timer)
        else:
            self.game_over()

    def check_apple_collision(self):
        pass

    def game_over(self):
        pass

    def move_snake(self):
        pass

    def check_collision(self):
        pass

    def draw_score(self):
        pass

    def on_key_press(self, e):
        """Controls direction variables with cursor keys"""
        key = e.keysym
        
        LEFT_CURSOR_KEY = "Left"
        if key == LEFT_CURSOR_KEY and self.move_x <= 0:
            self.move_x = -Cons.DOT_SIZE
            self.move_y = 0
        
        RIGHT_CURSOR_KEY = "Right"
        if key == RIGHT_CURSOR_KEY and self.move_x >= 0:
            self.move_x = Cons.DOT_SIZE
            self.move_y = 0

        UP_CURSOR_KEY = "Up"
        if key == UP_CURSOR_KEY and self.move_y <= 0:
            self.move_x = 0
            self.move_y = -Cons.DOT_SIZE
        
        DOWN_CURSOR_KEY = "Down"
        if key == DOWN_CURSOR_KEY and self.move_y >= 0:
            self.move_x = 0
            self.move_y = Cons.DOT_SIZE

    def locate_apple(self):
        """Places the apple object on Canvas"""
        apple = self.find_withtag("apple")
        self.delete(apple[0])
        r = random.randint(0, Cons.MAX_RAND_POS)
        self.apple_x = r * Cons.DOT_SIZE
        r = random.randint(0, Cons.MAX_RAND_POS)
        self.apple_y = r * Cons.DOT_SIZE
        self.create_image(self.apple_x, self.apple_y, anchor=NW, image=self.apple, tag="apple")


    def create_objects(self):
        """Create objects on Canvas"""
        self.create_text(30, 10, text="Score: {0}".format(self.score), tag="score", fill="white")
        self.create_image(self.apple_x, self.apple_y, image=self.apple, anchor=NW, tag="apple")
        self.create_image(50, 50, image=self.head, anchor=NW, tag="head")
        self.create_image(40, 50, image=self.body, anchor=NW, tag="body")
        self.create_image(30, 50, image=self.body, anchor=NW, tag="body")        

    def load_images(self):
        """Load images from disk"""
        try:
            self.ibody = Image.open("res/body.png")
            self.ihead = Image.open("res/head.png")
            self.iapple = Image.open("res/apple.png")
            self.body = ImageTk.PhotoImage(self.ibody)
            self.head = ImageTk.PhotoImage(self.ihead)
            self.apple = ImageTk.PhotoImage(self.iapple)

        except IOError as e:
            print(e)
            sys.exit(1)


class Snake(Frame):

    def __init__(self, master):
        super(Snake, self).__init__(master)
        self.master.title("Snake Game")
        self.board = Board()
        self.pack()


def main():
    root = Tk()
    root.geometry(str.format("{}x{}", Cons.BOARD_WIDTH, Cons.BOARD_HEIGHT))
    root.resizable(0, 0)
    snake = Snake(root)

    root.mainloop()

main()
