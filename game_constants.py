import pygame
import os

WIDTH, HEIGHT = 800, 600  # resolution/game area

WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # window for everything to be displayed
pygame.display.set_caption("Ethan's Space Invaders")
pygame.display.set_icon(pygame.image.load(os.path.join("Assets", "spaceship_yellow.png")))

WHITE = (255, 255, 255)  # for convenience
BLACK = (0, 0, 0)
RED = (200, 0, 0)
GREEN = (0, 255, 0)

SPACE_IMAGE = pygame.image.load(os.path.join("Assets", "space.png"))  # background
SPACE = pygame.transform.scale(SPACE_IMAGE, (WIDTH, HEIGHT))

PLAYER_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets", "spaceship_yellow.png"))  # player image and rectangle
PLAYER_SPACESHIP_WIDTH = 55
PLAYER_SPACESHIP_HEIGHT = 40
PLAYER_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(PLAYER_SPACESHIP_IMAGE,
                           (PLAYER_SPACESHIP_WIDTH, PLAYER_SPACESHIP_HEIGHT)), 180)

PLAYER_SPACESHIP_x, PLAYER_SPACESHIP_y = WIDTH / 2 - round(PLAYER_SPACESHIP_WIDTH / 2), HEIGHT - (  # start spawn
            PLAYER_SPACESHIP_HEIGHT * 2)

ENEMY_IMAGE = pygame.image.load(os.path.join("Assets", "spaceship_red.png"))  # enemy image and rectangle size
ENEMY_WIDTH = 35
ENEMY_HEIGHT = 23
ENEMY = pygame.transform.scale(ENEMY_IMAGE, (ENEMY_WIDTH, ENEMY_HEIGHT))

ENEMY_SPEED = 1
ENEMY_BULLET_SPEED = 4

BULLET_SPEED = 12
BULLET_WIDTH = 3
BULLET_HEIGHT = 15

FPS = 60
VEL = 7
FIRE_RATE = 10  # decrease value to increase rate (based on frames)

# VALUES BELOW AND TO END OF FILE CHANGE AS PROGRAM IS RUN (global values)
bullet_timer = 0  # keep at zero, for player

CURRENT_ENEMY = 0  # for level spawner

PLAYER_SET_HEALTH = 12  # health and score, can change initial values here
PLAYER_HEALTH = PLAYER_SET_HEALTH
PLAYER_SCORE = 0

GAME_COMPLETED = False  # tracks whether game passed by player, keep at false
