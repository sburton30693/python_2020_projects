# Spencer Burton
# 3/5/2021

# Imports #################################################
import pygame as pg
import random as r
import math
from os import *


# Game Object Classes ####################################

class Player(pg.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pg.Surface((50, 40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.bottom = (HEIGHT - (HEIGHT * 0.1))
        self.speedx = 0
        self.speed_num = 5

    def update(self):
        key_states = pg.key.get_pressed()

        self.speedx = 0

        if key_states[pg.K_RIGHT]:
            self.speedx = self.speed_num
        if key_states[pg.K_LEFT]:
            self.speedx = -self.speed_num

        self.rect.x += self.speedx

        # Keep from leaving the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        

class NPC(pg.sprite.Sprite):
    def __init__(self):
        super(NPC, self).__init__()
        self.image = pg.Surface((25, 25))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.top = 0
        self.speedy = 2

    def update(self):
        self.rect.y += self.speedy

        if self.rect.top > HEIGHT:
            self.rect.centery = r.randint(0, HEIGHT)


# Game Constants #########################################
WIDTH = 600
HEIGHT = 900
FPS = 60

# Colors (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
PINK = (255, 125, 220)
PURPLE = (153, 0, 255)
LIME = (100, 255, 0)

title = "Shmup"


# Initialize Pygame #######################################
pg.init()
pg.mixer.init()

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption(title)
clock = pg.time.Clock()


# Load Images #############################################


# Create Sprite Groups ####################################
all_sprites = pg.sprite.Group()
player_group = pg.sprite.Group()
npc_group = pg.sprite.Group()

# Create Game Objects #####################################
player = Player()
npc = NPC()

# Add Objects to Sprite Groups ############################
player_group.add(player)
npc_group.add(npc)

for i in player_group:
    all_sprites.add(i)
for i in npc_group:
    all_sprites.add(i)

# Game Loop ###############################################

# Game Update Variables
running = True

while running:
    # Timing
    clock.tick(FPS)

    # Handle Events / Collect Inputs
    for event in pg.event.get():
        if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            running = False
        if event.type == pg.QUIT:
            running = False

    # Update
    all_sprites.update()

    # Draw / Render
    screen.fill(BLACK)
    all_sprites.draw(screen)

    pg.display.flip()


# Quit
pg.quit()
