from game_constants import *
from random import randint
from abc import abstractmethod
from math import sin, sqrt


# PARENT ABSTRACT CLASS
class Enemy:
    def __init__(self, rectangle):
        self.rectangle = rectangle  # pygame rectangle ('hit box')
        self.gun_timer = 0
        self.score = 0
        # must also specify self.health, for hit points of each enemy

    @abstractmethod
    def movement(self):  # movement based on math function and frames
        pass

    @abstractmethod
    def gunfire(self, enemy_bullets):  # add bullet to list based on fire rate from frame rate
        pass

    @abstractmethod  # must be class method when defined specifically for each enemy type. spawn rate from spawn pattern
    def spawn_timer(self, spawn_rate):
        pass


class Enemy1(Enemy):
    Enemy1_spawn_timer = 0

    def __init__(self, rectangle):
        Enemy.__init__(self, rectangle)
        self.direction = randint(0, 1)  # will randomly start going left or right
        self.health = 1
        self.score = 60

    def movement(self):  # square root movement pattern ('jumps' from edges of screen)
        self.rectangle.y += ENEMY_SPEED
        if self.direction == 1:
            self.rectangle.x += round(sqrt(WIDTH - self.rectangle.x) / 3)
            if self.rectangle.x >= WIDTH - ENEMY_WIDTH:
                self.direction = 0
        if self.direction == 0:
            self.rectangle.x -= round(sqrt(self.rectangle.x) / 3)
            if self.rectangle.x <= 5:
                self.direction = 1

    def gunfire(self, enemy_bullets):
        self.gun_timer += 1
        if self.gun_timer > 90:
            bullet = pygame.Rect(self.rectangle.x + ENEMY_WIDTH / 2, self.rectangle.y + ENEMY_HEIGHT, BULLET_WIDTH,
                                 BULLET_HEIGHT)
            enemy_bullets.append(bullet)
            self.gun_timer = 0

    @classmethod
    def spawn_timer(cls, spawn_rate):
        cls.Enemy1_spawn_timer += 1
        if cls.Enemy1_spawn_timer >= spawn_rate:
            cls.Enemy1_spawn_timer = 0
            return True
        else:
            return False


class Enemy2(Enemy):
    Enemy2_spawn_timer = 0

    def __init__(self, rectangle):
        Enemy.__init__(self, rectangle)
        self.health = 3
        self.unique_speed = 0
        self.score = 80

    def movement(self):  # moves at 0.5 pixel speed per frame (standard is 1)
        if self.unique_speed == 0:
            self.unique_speed = 1
        elif self.unique_speed == 1:
            self.unique_speed = 0
        self.rectangle.y += self.unique_speed

    def gunfire(self, enemy_bullets):
        self.gun_timer += 1
        if self.gun_timer > 180:
            bullet = pygame.Rect(self.rectangle.x + ENEMY_WIDTH / 2, self.rectangle.y + ENEMY_HEIGHT, BULLET_WIDTH,
                                 BULLET_HEIGHT)
            enemy_bullets.append(bullet)
            self.gun_timer = 0

    @classmethod
    def spawn_timer(cls, spawn_rate):
        cls.Enemy2_spawn_timer += 1
        if cls.Enemy2_spawn_timer >= spawn_rate:
            cls.Enemy2_spawn_timer = 0
            return True
        else:
            return False


class Enemy3(Enemy):
    Enemy3_spawn_timer = 0

    def __init__(self, rectangle):
        Enemy.__init__(self, rectangle)
        self.direction = randint(0, 1)  # will randomly start going left or right
        self.sin_value = 1
        self.sin_value_timer = 0
        self.health = 2
        self.score = 70

    def sin_value_modifier(self):  # unique movement procedure for this enemy for its sine function
        self.sin_value_timer += 1
        if self.sin_value_timer >= 30:
            self.sin_value += 1
            self.sin_value_timer = 0

    def movement(self):  # moves in a wave-like pattern (sine wave)
        self.rectangle.y += ENEMY_SPEED
        self.sin_value_modifier()
        if self.direction == 1:
            self.rectangle.x += abs(round(sin(self.sin_value) * 3))
            if self.rectangle.x >= WIDTH - ENEMY_WIDTH:
                self.direction = 0
                self.sin_value = 1
        if self.direction == 0:
            self.rectangle.x -= abs(round(sin(self.sin_value) * 3))
            if self.rectangle.x <= 5:
                self.direction = 1
                self.sin_value = 1

    def gunfire(self, enemy_bullets):
        self.gun_timer += 1
        if self.gun_timer > 180:
            bullet = pygame.Rect(self.rectangle.x + ENEMY_WIDTH / 2, self.rectangle.y + ENEMY_HEIGHT, BULLET_WIDTH,
                                 BULLET_HEIGHT)
            enemy_bullets.append(bullet)
            self.gun_timer = 0

    @classmethod
    def spawn_timer(cls, spawn_rate):
        cls.Enemy3_spawn_timer += 1
        if cls.Enemy3_spawn_timer >= spawn_rate:
            cls.Enemy3_spawn_timer = 0
            return True
        else:
            return False
