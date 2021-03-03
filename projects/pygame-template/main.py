# Spencer Burton
# 2/23/2021

# Imports
import pygame
import random
import os


# Setup folder Assets
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "imgs")
snd_folder = os.path.join(game_folder, "snds")

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
        self.key_pressed = False
        self.mouse_button_held = False

    def update(self):
        # self.speed[0] = 0
        # self.speed[1] = 0

        if self.mouse_button_held:
            self.rect.center = pygame.mouse.get_pos()

        keystate = pygame.key.get_pressed()

        # if keystate[pygame.K_LEFT]:
        #     self.speed[0] = -5
        # if keystate[pygame.K_RIGHT]:
        #     self.speed[0] = 5
        # if keystate[pygame.K_UP]:
        #     self.speed[1] = -5
        # if keystate[pygame.K_DOWN]:
        #     self.speed[1] = 5

        self.rect.x += self.speed[0] * self.speed_num
        self.rect.y += self.speed[1] * self.speed_num

        # Bind player to screen
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= WIDTH:
            self.rect.right = WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT


def spawn_new_player(x, y, all_sprites, players_group):
    new_player = Player()
    new_player.rect.center = (x, y)
    new_player.speed[0] = random.randint(-5, 5)
    new_player.speed[1] = random.randint(-5, 5)
    all_sprites.add(new_player)
    players_group.add(new_player)


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

            if event.type == pygame.MOUSEBUTTONDOWN and player.rect.collidepoint(pygame.mouse.get_pos()):
                player.mouse_button_held = True
            if event.type == pygame.MOUSEBUTTONUP:
                player.mouse_button_held = False
                spawn_new_player(player.rect.centerx, player.rect.centery, all_sprites, players_group)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

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
