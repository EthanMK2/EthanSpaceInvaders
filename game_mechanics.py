from game_animations import *
from time import sleep
# this file uses/modifies global variables from the game_constants file


# spawn_pattern = [ (Enemy_Class, x_coordinate_spawn, wait_time_in_seconds), (), ()... ]
def level_spawner(enemy_list, spawn_pattern):  # streamline way to make the level in main
    global CURRENT_ENEMY
    if CURRENT_ENEMY >= len(spawn_pattern):
        return

    enemy_class = spawn_pattern[CURRENT_ENEMY][0]
    x_cor = spawn_pattern[CURRENT_ENEMY][1]
    wait_frames = round(spawn_pattern[CURRENT_ENEMY][2] * FPS)

    if enemy_class.spawn_timer(wait_frames) is True:  # add enemy to list and go to next enemy timer in spawn_pattern
        enemy = enemy_class(pygame.Rect(x_cor, -50, ENEMY_WIDTH, ENEMY_HEIGHT))
        enemy_list.append(enemy)
        CURRENT_ENEMY += 1


def handle_enemy_gunfire_movement(enemy_bullets, player):  # extra function to emphasize gunfire movement and collision
    global PLAYER_HEALTH
    for bullet in enemy_bullets:
        bullet.y += ENEMY_BULLET_SPEED
        if bullet.y > HEIGHT:
            enemy_bullets.remove(bullet)
        if bullet.colliderect(player):
            enemy_bullets.remove(bullet)  # strange crash: when you hit bullet RIGHT at bottom, it crashes. (draw WIN?)
            PLAYER_HEALTH -= 1


def handle_enemy(enemy_list, enemy_bullets, player, player_bullets):  # handle enemy movement, gunfire, and collisions
    global PLAYER_HEALTH
    global PLAYER_SCORE
    for enemy in enemy_list:
        enemy.movement()
        enemy.gunfire(enemy_bullets)
    for enemy in enemy_list:
        if enemy.rectangle.colliderect(player):
            enemy_list.remove(enemy)
            PLAYER_HEALTH -= 1
    for enemy in enemy_list:
        if enemy.rectangle.y > HEIGHT:
            enemy_list.remove(enemy)
    for bullet in player_bullets:
        for enemy in enemy_list:
            if bullet.colliderect(enemy.rectangle):
                if bullet in player_bullets:  # this is because if bullet hits more than one, it removes twice (crash)
                    player_bullets.remove(bullet)
                    enemy.health -= 1
                if enemy.health <= 0:
                    PLAYER_SCORE += enemy.score  # handles scoring for enemy killed
                    ExplosionAnimation(enemy.rectangle.x, enemy.rectangle.y)
                    enemy_list.remove(enemy)


def draw_window(player, enemy_list, player_bullets, enemy_bullets):  # displays everything the player sees
    WIN.blit(SPACE, (0, 0))  # background
    WIN.blit(PLAYER_SPACESHIP, (player.x, player.y))  # player

    # displays health, score, and controls
    font = pygame.font.SysFont("freesansbold", 14)
    score_text = font.render(f"Space: Fire    Arrow keys: Move", True, GREEN, None)
    WIN.blit(score_text, (10, 575))

    font = pygame.font.SysFont("freesansbold", 20)
    health_text = font.render(f"Health: {PLAYER_HEALTH}", True, GREEN, BLACK)
    WIN.blit(health_text, (10, 20))

    font = pygame.font.SysFont("freesansbold", 20)
    score_text = font.render(f"Score: {PLAYER_SCORE}", True, GREEN, BLACK)
    WIN.blit(score_text, (600, 20))

    # draw animations (see game_animations for implementation)
    ExplosionAnimation.explosion_animations()

    # draw enemies and bullets
    for enemy in enemy_list:
        WIN.blit(ENEMY, (enemy.rectangle.x, enemy.rectangle.y))

    for bullet in player_bullets:
        pygame.draw.rect(WIN, GREEN, bullet)

    for bullet in enemy_bullets:
        pygame.draw.rect(WIN, RED, bullet)

    if PLAYER_HEALTH <= 0:  # Lose message
        game_over_font = pygame.font.SysFont("freesansbold", 30)
        game_over_message = game_over_font.render(f"GAME OVER", True, WHITE, None)
        WIN.blit(game_over_message, (WIDTH // 2 - game_over_message.get_width()//2, HEIGHT // 2))  # centered

    if GAME_COMPLETED:  # Win message
        game_completed_font = pygame.font.SysFont("freesansbold", 30)
        game_completed_message = game_completed_font.render(f"GAME COMPLETE", True, WHITE, None)
        WIN.blit(game_completed_message, (WIDTH // 2 - game_completed_message.get_width() // 2, HEIGHT // 2))  # center

    pygame.display.update()


def player_movement(player):  # movement and screen barriers
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_LEFT]:
        if player.x > 4:
            player.x -= VEL
    if keys_pressed[pygame.K_RIGHT]:
        if player.x < WIDTH - PLAYER_SPACESHIP_WIDTH:
            player.x += VEL
    if keys_pressed[pygame.K_UP]:
        if player.y > 0:
            player.y -= VEL
    if keys_pressed[pygame.K_DOWN]:
        if player.y < HEIGHT - PLAYER_SPACESHIP_HEIGHT:
            player.y += VEL


def handle_player_bullets(player, player_bullets):  # player's bullet fire rate and off screen
    global bullet_timer
    firing_button = pygame.key.get_pressed()
    bullet_timer += 1
    if firing_button[pygame.K_SPACE]:
        if bullet_timer > FIRE_RATE:
            # bullets placed at middle and up from spaceship. this ugliness maintains customizable constants
            bullet = pygame.Rect(player.x + PLAYER_SPACESHIP_WIDTH // 2 - BULLET_WIDTH // 2,
                                 player.y - BULLET_HEIGHT, BULLET_WIDTH, BULLET_HEIGHT)
            player_bullets.append(bullet)
            bullet_timer = 0
    for bullet in player_bullets:
        bullet.y -= BULLET_SPEED
        if bullet.y < 0:
            player_bullets.remove(bullet)


def game_done(player, enemy_list, player_bullets, enemy_bullets, spawn_pattern):  # indicates when player passes or dies
    global PLAYER_HEALTH  # for resetting values
    global GAME_COMPLETED
    global CURRENT_ENEMY
    global PLAYER_SCORE
    if PLAYER_HEALTH <= 0:  # GAME OVER and reset
        draw_window(player, enemy_list, player_bullets, enemy_bullets)
        sleep(4)
        PLAYER_HEALTH = PLAYER_SET_HEALTH
        CURRENT_ENEMY = 0
        PLAYER_SCORE = 0
        return True
    if len(spawn_pattern) == CURRENT_ENEMY and len(enemy_list) == 0:  # GAME COMPLETED and reset
        GAME_COMPLETED = True
        draw_window(player, enemy_list, player_bullets, enemy_bullets)
        sleep(4)
        PLAYER_HEALTH = PLAYER_SET_HEALTH
        CURRENT_ENEMY = 0
        PLAYER_SCORE = 0
        GAME_COMPLETED = False
        return True
