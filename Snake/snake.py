import random
import os

WIDTH = 60
HEIGHT = 30
snake_char = "@"
fence_char = "*"
snake_x = random.randint(1, WIDTH - 2)
snake_y = random.randint(1, HEIGHT - 2)
game_over = False


def print_game():
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if x == 0 or x == WIDTH - 1 or y == 0 or y == HEIGHT - 1:
                print(fence_char, end='')
            elif x == snake_x and y == snake_y:
                print(snake_char, end='')
            else:
                print(" ", end='')
        print()
    print("Hova?")


def move_snake(direction):
    global snake_x, snake_y, game_over

    if direction == "balra":
        snake_x -= 1
    elif direction == "jobbra":
        snake_x += 1
    elif direction == "fel":
        snake_y -= 1
    elif direction == "le":
        snake_y += 1
    elif direction == "meguntam":
        game_over = True

    if (
            snake_x == 0 or
            snake_x == WIDTH - 1 or
            snake_y == 0 or
            snake_y == HEIGHT - 1
    ):
        game_over = True


print_game()
while not game_over:
    user_input = input()
    move_snake(user_input)
    if not game_over:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_game()

print("Most ennyi volt, szép napot!")