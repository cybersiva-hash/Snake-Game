import pygame
import random

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)

WIDTH, HEIGHT = 600, 400
GAME_DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

SNAKE_SIZE = 10
SNAKE_SPEED = 15

message_font = pygame.font.SysFont("ubuntu", 30)
score_font = pygame.font.SysFont("ubuntu", 25)

def print_score(score):
    text = score_font.render("Score: " + str(score), True, ORANGE)
    GAME_DISPLAY.blit(text, [0, 0])


def draw_snake(snake_pixels):
    for pixel in snake_pixels:
        pygame.draw.rect(GAME_DISPLAY, WHITE, [pixel[0], pixel[1], SNAKE_SIZE, SNAKE_SIZE])


def spawn_food(snake_pixels):
    while True:
        x = random.randrange(0, WIDTH - SNAKE_SIZE, SNAKE_SIZE)
        y = random.randrange(0, HEIGHT - SNAKE_SIZE, SNAKE_SIZE)
        if [x, y] not in snake_pixels:
            return x, y


def game_over_screen(score):
    while True:
        GAME_DISPLAY.fill(BLACK)
        msg1 = message_font.render("GAME OVER!", True, RED)
        msg2 = message_font.render("Press R to Restart or Q to Quit", True, WHITE)

        GAME_DISPLAY.blit(msg1, [WIDTH // 3.2, HEIGHT // 3])
        GAME_DISPLAY.blit(msg2, [WIDTH // 6, HEIGHT // 2])
        print_score(score)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_r:
                    return


def run_game():
    while True:

        x = WIDTH // 2
        y = HEIGHT // 2
        x_speed = 0
        y_speed = 0

        snake_pixels = []
        snake_length = 1

        target_x, target_y = spawn_food(snake_pixels)

        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and x_speed == 0:
                        x_speed = -SNAKE_SIZE
                        y_speed = 0
                    elif event.key == pygame.K_RIGHT and x_speed == 0:
                        x_speed = SNAKE_SIZE
                        y_speed = 0
                    elif event.key == pygame.K_UP and y_speed == 0:
                        y_speed = -SNAKE_SIZE
                        x_speed = 0
                    elif event.key == pygame.K_DOWN and y_speed == 0:
                        y_speed = SNAKE_SIZE
                        x_speed = 0

            if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
                break

            x += x_speed
            y += y_speed

            GAME_DISPLAY.fill(BLACK)

            pygame.draw.rect(GAME_DISPLAY, ORANGE, [target_x, target_y, SNAKE_SIZE, SNAKE_SIZE])

            snake_pixels.append([x, y])
            if len(snake_pixels) > snake_length:
                del snake_pixels[0]

            if len(snake_pixels) > 3:
                if [x, y] in snake_pixels[:-1]:
                    break

            draw_snake(snake_pixels)
            print_score(snake_length - 1)
            pygame.display.update()

            if x == target_x and y == target_y:
                snake_length += 1
                target_x, target_y = spawn_food(snake_pixels)

            clock.tick(SNAKE_SPEED)

        game_over_screen(snake_length - 1)


run_game()
