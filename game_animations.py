from game_constants import *


class ExplosionAnimation:  # object keeps track of each individual animation on screen
    explosion_list = []

    def __init__(self, x_coordinate, y_coordinate):  # location on screen to spawn, and adds itself to list
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.animation_frame = 0
        ExplosionAnimation.explosion_list.append(self)

    """
    this method loops through the list of animations that are to be displayed/are displaying. it loops through each
    object animation_frame to determine which animation image to display, based on 60 frames per second. when an
    animation object reaches an animation_frame factor of 10 (5 frames in time), it will display the next image
    in that index of the list of animation images.
    """
    @classmethod
    def explosion_animations(cls):
        for explosion in cls.explosion_list:
            explosion.animation_frame += 2
            animation_index = explosion.animation_frame // 10
            if animation_index <= len(EXPLOSION_FRAMES) - 1:
                WIN.blit(EXPLOSION_FRAMES[animation_index], (explosion.x_coordinate, explosion.y_coordinate))
        for explosion in cls.explosion_list:
            if explosion.animation_frame // 10 >= len(EXPLOSION_FRAMES) - 1:  # when done displaying, remove from list
                cls.explosion_list.remove(explosion)


# Explosion animation images
EXPLOSION_1 = pygame.image.load(os.path.join("Assets", "explosion1.png"))
EXPLOSION_2 = pygame.image.load(os.path.join("Assets", "explosion2.png"))
EXPLOSION_3 = pygame.image.load(os.path.join("Assets", "explosion3.png"))
EXPLOSION_4 = pygame.image.load(os.path.join("Assets", "explosion4.png"))
EXPLOSION_5 = pygame.image.load(os.path.join("Assets", "explosion5.png"))
EXPLOSION_6 = pygame.image.load(os.path.join("Assets", "explosion6.png"))
EXPLOSION_FRAMES = [
    pygame.transform.scale(EXPLOSION_1, (ENEMY_WIDTH, ENEMY_HEIGHT)),
    pygame.transform.scale(EXPLOSION_2, (ENEMY_WIDTH, ENEMY_HEIGHT)),
    pygame.transform.scale(EXPLOSION_3, (ENEMY_WIDTH, ENEMY_HEIGHT)),
    pygame.transform.scale(EXPLOSION_4, (ENEMY_WIDTH, ENEMY_HEIGHT)),
    pygame.transform.scale(EXPLOSION_5, (ENEMY_WIDTH, ENEMY_HEIGHT)),
    pygame.transform.scale(EXPLOSION_6, (ENEMY_WIDTH, ENEMY_HEIGHT)),
]