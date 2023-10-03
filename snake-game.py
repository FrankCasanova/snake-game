import pygame
import random

# Pygame initialization
pygame.init()

# Definition of colors
WHITE = (255, 255, 255)
YELLOW = (255, 255, 102)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

# Screen Settings
DIS_WIDTH = 600
DIS_HEIGHT = 400
DIS = pygame.display.set_mode((DIS_WIDTH, DIS_HEIGHT))
pygame.display.set_caption('Snake Game In Python')

# Game settings
SNAKE_BLOCK = 10
SNAKE_SPEED = 15

# Fonts
FONT_STYLE = pygame.font.SysFont('bahnschrift', 25)
SCORE_FONT = pygame.font.SysFont('comicsansms', 35)

def your_score(score: int) -> None:
    """Shows the score on the screen."""
    value = SCORE_FONT.render('Your Score: ' + str(score), True, YELLOW)
    DIS.blit(value, [0, 0])

def our_snake(snake_block: int, snake_list: list) -> None:
    """Draw the snake on the screen."""
    for x, y in snake_list:
        pygame.draw.rect(DIS, BLACK, [x, y, snake_block, snake_block])

def message(msg: str, color: tuple) -> None:
    """Displays a message on the screen."""
    mesg = FONT_STYLE.render(msg, True, color)
    DIS.blit(mesg, (DIS_WIDTH / 6, DIS_HEIGHT / 3)) 

def game_loop() -> None:
    """Main game loop."""
    game_over = False
    game_close = False

    x1, y1 = DIS_WIDTH / 2, DIS_HEIGHT / 2
    x1_change, y1_change = 0, 0

    snake_list = []
    length_snake = 1

    foodx = round(random.randrange(0, DIS_WIDTH - SNAKE_BLOCK) / 10.0) * 10.0
    foody = round(random.randrange(0, DIS_HEIGHT - SNAKE_BLOCK) / 10.0) * 10.0

    while not game_over:
        while game_close:
            DIS.fill(BLUE)
            message('You Lost! Press "C" to play again or "Q" to quit the game', RED)
            your_score(length_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -SNAKE_BLOCK
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = SNAKE_BLOCK
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -SNAKE_BLOCK
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = SNAKE_BLOCK
                    x1_change = 0

        if x1 >= DIS_WIDTH or x1 < 0 or y1 >= DIS_HEIGHT or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change

        DIS.fill(BLUE)
        pygame.draw.rect(DIS, GREEN, [foodx, foody, SNAKE_BLOCK, SNAKE_BLOCK])
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_snake:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        our_snake(SNAKE_BLOCK, snake_list)
        your_score(length_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, DIS_WIDTH - SNAKE_BLOCK) / 10.0) * 10.0
            foody = round(random.randrange(0, DIS_HEIGHT - SNAKE_BLOCK) / 10.0) * 10.0
            length_snake += 1

        pygame.time.Clock().tick(SNAKE_SPEED)

    pygame.quit()
    quit()

if __name__ == "__main__":
    game_loop()