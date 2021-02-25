# Spencer Burton
# 2/23/2021

# Imports
import pygame
import random
import math


# Constants
WIDTH = 480
HEIGHT = 360
TITLE = "Template"
FPS = 30

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


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.Surface((25, 25))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.theta = 330
        self.speed_num = 1
        self.speed = (self.speed_num, 0)

    def update(self):
        #rad = self.theta * math.pi/180
        #self.rect.y += -math.sin(rad) * 5
        #self.rect.x += math.cos(rad) * 5
        #self.theta += 2
        self.rect.x += self.speed[0] * self.speed_num
        self.rect.y += self.speed[1] * self.speed_num
        self.speed_num += 0.25


        #if self.rect.left > WIDTH:
        #    self.rect.right = 0
        #if self.rect.right < 0:
        #    self.rect.left = WIDTH
        #if self.rect.top > HEIGHT:
        #    self.rect.bottom = 0
        #if self.rect.bottom < 0:
        #    self.rect.top = HEIGHT

        if self.rect.left > WIDTH: # Right side
            self.rect.top = HEIGHT
            self.rect.centerx = WIDTH / 2
            self.speed = (0, -1)
        if self.rect.right < 0: # Left side
            self.rect.bottom = 0
            self.rect.centerx = WIDTH / 2
            self.speed = (0, 1)
        if self.rect.top > HEIGHT: # Bottom
            self.rect.left = WIDTH
            self.rect.centery = HEIGHT / 2
            self.speed = (-1, 0)
        if self.rect.bottom < 0: # Top
            self.rect.right = 0
            self.rect.centery = HEIGHT / 2
            self.speed = (1, 0)


# Main Function
def main():
    # Initialize PyGame and create a window
    pygame.init()
    pygame.mixer.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(TITLE)

    clock = pygame.time.Clock()

    # Sprite Groups
    all_sprites = pygame.sprite.Group()
    players_group = pygame.sprite.Group()
    mobs_group = pygame.sprite.Group()

    # Create Game Objects and add to sprite groups
    player = Player()
    all_sprites.add(player)
    players_group.add(player)

    # Game Loop
    running = True
    while running:
        # Keep loop running at the right speed
        clock.tick(FPS)

        # Process Input
        for event in pygame.event.get():
            # Check for closing window
            if event.type == pygame.QUIT:
                running = False

        # Update Everything
        all_sprites.update()

        # Render all changes
        screen.fill(CYAN)
        all_sprites.draw(screen)
        pygame.display.flip()


main()
