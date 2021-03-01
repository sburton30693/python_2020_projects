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


class Npc(pygame.sprite.Sprite):
    def __init__(self):
        super(Npc, self).__init__()
        self.image = pygame.Surface((25, 25))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        #self.rect.bottomright = (0, 0)
        self.theta = 0
        self.speed_num = 5
        self.acc = 0
        self.speed = [1, 1]
        self.do_circle = False

    def update(self):
        #rad = self.theta * math.pi/180
        #self.rect.centery = -math.sin(rad) * 20 + self.rect.centery
        #self.rect.centerx = math.cos(rad) * 20 + self.rect.centerx
        #self.theta += 20
        self.rect.x += self.speed[0] * self.speed_num
        self.rect.y += self.speed[1] * self.speed_num

        if self.rect.right > WIDTH:
            self.speed[0] *= -1
        #    self.rect.right = WIDTH
        #    self.speed[0] = 0
        #    self.speed[1] = -1
            self.image.fill(RED)
            self.speed_num += self.acc
        if self.rect.top < 0:
            self.speed[1] *= -1
        #    self.rect.top = 0
        #    self.speed[0] = -1
        #    self.speed[1] = 0
            self.image.fill(GREEN)
            self.speed_num += self.acc
        if self.rect.left < 0:
            self.speed[0] *= -1
        #    self.rect.left = 0
        #    self.speed[0] = 0
        #    self.speed[1] = 1
            self.image.fill(BLUE)
            self.speed_num += self.acc
        if self.rect.bottom > HEIGHT:
            self.speed[1] *= -1
        #    self.rect.bottom = HEIGHT
        #    self.speed[0] = 1
        #    self.speed[1] = 0
            self.image.fill(PURPLE)
            self.speed_num += self.acc

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.speed_num = 5
        self.speed = [0, 0]

    def update(self):
        self.rect.x += self.speed[0] * self.speed_num
        self.rect.y += self.speed[1] * self.speed_num


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
    npc = Npc()
    player = Player()

    # Add to sprite groups
    all_sprites.add(npc)
    mobs_group.add(npc)
    all_sprites.add(player)
    players_group.add(player)

    # Game Loop
    running = True
    while running:
        # Keep loop running at the right speed
        clock.tick(FPS)

        # Process Input
        for event in pygame.event.get():

            # Basic grid movement
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.rect.x -= 50
                if event.key == pygame.K_RIGHT:
                    player.rect.x += 50
                if event.key == pygame.K_UP:
                    player.rect.y -= 50
                if event.key == pygame.K_DOWN:
                    player.rect.y += 50

                # Flow movement
                #if event.key == pygame.K_LEFT:
                #    player.speed[0] = -1
                #if event.key == pygame.K_RIGHT:
                #    player.speed[0] = 1
                #if event.key == pygame.K_UP:
                #    player.speed[1] = -1
                #if event.key == pygame.K_DOWN:
                #    player.speed[1] = 1

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player.speed[0] = 0
                if event.key == pygame.K_UP or event.key == pygame.K_LEFT:
                    player.speed[1] = 0

            # Check for closing window
            if event.type == pygame.QUIT:
                running = False

        # Update Everything
        all_sprites.update()

        # Render all changes
        screen.fill(CYAN)  # Disable for art
        all_sprites.draw(screen)
        pygame.display.flip()


main()
