from sys import exit

import game_mechanics
from game_enemies import *

pygame.init()


def main():
    enemy_list = []  # tracks enemies
    player = pygame.Rect(PLAYER_SPACESHIP_x, PLAYER_SPACESHIP_y, PLAYER_SPACESHIP_WIDTH, PLAYER_SPACESHIP_HEIGHT)
    player_bullets = []  # tracks bullets
    enemy_bullets = []

    run = True
    clock = pygame.time.Clock()

    # level design. KEY: (enemyType, x-coordinateSpawnLocation, spawnDelaySeconds)
    spawn_pattern = [
        (Enemy2, 150, 3), (Enemy2, 350, 1), (Enemy2, 550, 1),
        (Enemy2, 550, 3), (Enemy2, 350, 1), (Enemy2, 150, 1),
        (Enemy2, 150, 3), (Enemy2, 350, 1), (Enemy2, 550, 1),
        (Enemy2, 100, 4), (Enemy2, 200, 0), (Enemy2, 300, 0), (Enemy2, 400, 0), (Enemy2, 500, 0), (Enemy2, 600, 0),
        (Enemy2, 700, 0),  # type 2 intro end
        (Enemy1, 200, 10), (Enemy1, 600, 0),
        (Enemy1, 100, 4), (Enemy1, 400, 0), (Enemy1, 600, 0),
        (Enemy1, 100, 4), (Enemy1, 200, 0), (Enemy1, 600, 0), (Enemy1, 700, 0),
        (Enemy1, 100, 6), (Enemy1, 200, 0), (Enemy1, 300, 0), (Enemy1, 400, 0), (Enemy1, 500, 0), (Enemy1, 600, 0),
        (Enemy1, 700, 0),  # type 1 intro end
        (Enemy3, 400, 6), (Enemy3, 200, 3), (Enemy3, 600, 3),
        (Enemy3, 100, 6), (Enemy3, 200, 0), (Enemy3, 300, 0), (Enemy3, 400, 0), (Enemy3, 500, 0), (Enemy3, 600, 0),
        (Enemy3, 700, 6),  # type 3 intro end
    ]

    # MAIN GAME LOOP
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                exit()

        game_mechanics.player_movement(player)
        game_mechanics.draw_window(player, enemy_list, player_bullets, enemy_bullets)

        game_mechanics.handle_enemy(enemy_list, enemy_bullets, player, player_bullets)
        game_mechanics.handle_enemy_gunfire_movement(enemy_bullets, player)
        game_mechanics.handle_player_bullets(player, player_bullets)

        game_mechanics.level_spawner(enemy_list, spawn_pattern)

        if game_mechanics.game_done(player, enemy_list, player_bullets, enemy_bullets, spawn_pattern):  # done, so reset
            main()


main()
