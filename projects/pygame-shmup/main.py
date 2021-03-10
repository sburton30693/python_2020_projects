# Spencer Burton
# 3/5/2021

# Imports #################################################
import pygame as pg
import random as r
import math
from os import *


# Game Object Classes ####################################

class Bullet(pg.sprite.Sprite):
    def __init__(self, x, y, size=5):
        super(Bullet, self).__init__()
        self.image = pg.Surface((size, 20))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speed = -20

    def update(self):
        self.rect.y += self.speed

        # Kill bullet when it goes off the top of the screen
        if self.rect.bottom <= 0:
            self.kill()


class Player(pg.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pg.Surface((50, 40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.bottom = (HEIGHT - (HEIGHT * 0.1))
        self.speedx = 0
        self.speed_num = 10
        self.bullet_upd = 0
        self.req_upd = 5
        self.bullet_size = 5

    def update(self):
        key_states = pg.key.get_pressed()
        self.speedx = 0

        if key_states[pg.K_RIGHT] or key_states[pg.K_d]:
            self.speedx += self.speed_num
        if key_states[pg.K_LEFT] or key_states[pg.K_a]:
            self.speedx += -self.speed_num

        if key_states[pg.K_UP]:
            self.bullet_size += 1
        if key_states[pg.K_DOWN]:
            self.bullet_size -= 1

        # Fire a bullet if holding space
        if key_states[pg.K_SPACE]:
            self.shoot()
        else:
            self.bullet_upd -= 1

        self.rect.x += self.speedx

        # Keep from leaving the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

    def shoot(self):
        if self.bullet_upd <= 0:
            bullet = Bullet(self.rect.centerx, self.rect.top + 1, self.bullet_size)
            bullet_group.add(bullet)
            all_sprites.add(bullet)
            self.bullet_upd = self.req_upd
        else:
            self.bullet_upd -= 1


class NPC(pg.sprite.Sprite):
    def __init__(self):
        super(NPC, self).__init__()
        self.image = pg.Surface((25, 25))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.top = 0
        self.speed = [r.randint(-5, 5), r.randint(0, 20)]

    def update(self):
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]

        if self.rect.top > HEIGHT:
            self.rect.center = (WIDTH/2, 0)
            self.speed[0] = r.randint(-5, 5)
            self.speed[1] = r.randint(0, 20)

        if self.rect.bottom < 0:
            self.kill()

    def spawn(self):
        npc = NPC()
        npc_group.add(npc)
        all_sprites.add(npc)

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
bullet_group = pg.sprite.Group()

# Create Game Objects #####################################
player = Player()
for i in range(20):
    npc = NPC()
    npc_group.add(npc)

# Add Objects to Sprite Groups ############################
player_group.add(player)

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

    # If NPC hits player
    hits = pg.sprite.spritecollide(player, npc_group, True)
    if hits:
        npc.spawn()

    hits = pg.sprite.groupcollide(npc_group, bullet_group, True, True)
    for hit in hits:
        npc.spawn()

    # Draw / Render
    screen.fill(BLACK)
    all_sprites.draw(screen)

    pg.display.flip()


# Quit
pg.quit()
