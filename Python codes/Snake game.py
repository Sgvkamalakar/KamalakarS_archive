#pip install pygame
import pygame
import random
pygame.init()
window_width = 500
window_height = 500
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
font = pygame.font.SysFont(None, 25)
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
block_size = 10
snake_speed = 10
def display_score(score):
    score_text = font.render("Score: " + str(score), True, white)
    window.blit(score_text, [0, 0])
def draw_snake(snake_list):
    for block in snake_list:
        pygame.draw.rect(window, white, [block[0], block[1], block_size, block_size])
def game_loop():
    snake_head_x = window_width / 2
    snake_head_y = window_height / 2
    snake_list = [[snake_head_x, snake_head_y]]
    snake_length = 1
    food_x = round(random.randrange(0, window_width - block_size) / 10.0) * 10.0
    food_y = round(random.randrange(0, window_height - block_size) / 10.0) * 10.0
    direction = "right"
    score = 0
    game_running = True
    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = "left"
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                elif event.key == pygame.K_UP:
                    direction = "up"
                elif event.key == pygame.K_DOWN:
                    direction = "down"
        if direction == "left":
            snake_head_x -= block_size
        elif direction == "right":
            snake_head_x += block_size
        elif direction == "up":
            snake_head_y -= block_size
        elif direction == "down":
            snake_head_y += block_size
        if snake_head_x < 0 or snake_head_x >= window_width or snake_head_y < 0 or snake_head_y >= window_height:
            game_running = False
        for block in snake_list[1:]:
            if snake_head_x == block[0] and snake_head_y == block[1]:
                game_running = False
        if snake_head_x == food_x and snake_head_y == food_y:
            food_x = round(random.randrange(0, window_width - block_size) / 10.0) * 10.0
            food_y = round(random.randrange(0, window_height - block_size) / 10.0) * 10.0
            snake_length += 1
            score += 1
            # snake_speed+=0.1
        if len(snake_list) > snake_length:
            del snake_list[0]
        snake_list.append([snake_head_x, snake_head_y])
        window.fill(black)
        pygame.draw.rect(window, red, [food_x, food_y, block_size, block_size])
        draw_snake(snake_list)
        display_score(score)
        pygame.display.update()
        clock.tick(snake_speed)
    pygame.time.delay(1000)    
    pygame.quit()
game_loop()
