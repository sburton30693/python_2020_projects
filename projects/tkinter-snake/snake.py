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
    DELAY = 60
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
        
        if self.in_game:
            self.check_apple_collision()
            self.move_snake()
            self.after(Cons.DELAY, self.on_timer)
        else:
            self.game_over()

    def check_apple_collision(self):
        """Checks if the head of snake collides with apple"""
        apple = self.find_withtag("apple")
        head = self.find_withtag("head")
        x1, y1, x2, y2 = self.bbox(head)
        overlap = self.find_overlapping(x1, y1, x2, y2)

        for hit in overlap:
            if apple[0] == hit:
                self.score += 1
                x, y = self.coords(apple)
                self.create_image(x, y, image=self.body, anchor=NW, tag="body")
                self.locate_apple()

    def game_over(self):
        self.delete(ALL)
        self.create_text(self.winfo_width() / 2, self.winfo_height() / 2,
                         text="Game Over with score {0}".format(self.score), fill="white")

    def move_snake(self):
        """Move the Snake"""
        body = self.find_withtag("body")
        head = self.find_withtag("head")
        snake = body + head

        z = 0
        while z < len(snake) - 1:
            c1 = self.coords(snake[z])
            c2 = self.coords(snake[z + 1])
            self.move(snake[z], c2[0] - c1[0], c2[1] - c1[1])
            z += 1

        self.move(head, self.move_x, self.move_y)

    def check_collision(self):
        """Check for collisions"""
        body = self.find_withtag("body")
        head = self.find_withtag("head")

        x1, y1, x2, y2 = self.bbox(head)
        overlap = self.find_overlapping(x1, y1, x2, y2)

        for part in body:
            for hit in overlap:
                if hit == part:
                    self.in_game = False

        if x1 < 0:
            self.in_game = False
        if x1 > Cons.BOARD_WIDTH - Cons.DOT_SIZE:
            self.in_game = False
        if y1 < 0:
            self.in_game = False
        if y1 > Cons.BOARD_WIDTH - Cons.DOT_SIZE:
            self.in_game = False

    def draw_score(self):
        score = self.find_withtag("score")
        self.itemconfigure(score, text="Score: {0}".format(self.score))

    def on_key_press(self, e):
        """Controls direction variables with cursor keys"""
        key = e.keysym
        
        LEFT_CURSOR_KEY = "Left"
        RIGHT_CURSOR_KEY = "Right"
        UP_CURSOR_KEY = "Up"
        DOWN_CURSOR_KEY = "Down"

        if key == LEFT_CURSOR_KEY and self.move_x <= 0:
            self.move_x = -Cons.DOT_SIZE
            self.move_y = 0
            return

        if key == RIGHT_CURSOR_KEY and self.move_x >= 0:
            self.move_x = Cons.DOT_SIZE
            self.move_y = 0
            return

        if key == UP_CURSOR_KEY and self.move_y <= 0:
            self.move_x = 0
            self.move_y = -Cons.DOT_SIZE
            return

        if key == DOWN_CURSOR_KEY and self.move_y >= 0:
            self.move_x = 0
            self.move_y = Cons.DOT_SIZE
            return

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
