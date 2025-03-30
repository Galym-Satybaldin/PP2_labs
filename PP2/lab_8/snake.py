import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Set up display
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Snake settings
snake_block = 20
snake_speed = 15
snake_list = []
snake_length = 1
snake_x = width // 2
snake_y = height // 2
snake_dx = 0
snake_dy = 0

# Food settings
foods = []  # List to store multiple foods
food_weights = [1, 2, 3]  # Different food weights

# Game loop
clock = pygame.time.Clock()
running = True

def spawn_food():
    food_x = round(random.randrange(0, width - snake_block) / 20.0) * 20.0
    food_y = round(random.randrange(0, height - snake_block) / 20.0) * 20.0
    weight = random.choice(food_weights)
    spawn_time = time.time()  # Record spawn time
    return [food_x, food_y, weight, spawn_time]

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and snake_dx != snake_block:
                snake_dx = -snake_block
                snake_dy = 0
            elif event.key == pygame.K_RIGHT and snake_dx != -snake_block:
                snake_dx = snake_block
                snake_dy = 0
            elif event.key == pygame.K_UP and snake_dy != snake_block:
                snake_dx = 0
                snake_dy = -snake_block
            elif event.key == pygame.K_DOWN and snake_dy != -snake_block:
                snake_dx = 0
                snake_dy = snake_block

    # Move snake
    snake_x += snake_dx
    snake_y += snake_dy

    # Check boundaries
    if snake_x >= width or snake_x < 0 or snake_y >= height or snake_y < 0:
        running = False

    # Spawn new food randomly
    if random.randint(1, 100) < 5 and len(foods) < 3:  # 5% chance, max 3 foods
        foods.append(spawn_food())

    # Update snake
    snake_head = [snake_x, snake_y]
    snake_list.append(snake_head)
    if len(snake_list) > snake_length:
        del snake_list[0]

    # Check food collision and timer
    current_time = time.time()
    for food in foods[:]:
        if snake_x == food[0] and snake_y == food[1]:
            snake_length += food[2]  # Increase length by food weight
            foods.remove(food)
        # Remove food after 5 seconds
        elif current_time - food[3] > 5:
            foods.remove(food)

    # Draw everything
    screen.fill(BLACK)
    for x in snake_list:
        pygame.draw.rect(screen, GREEN, [x[0], x[1], snake_block, snake_block])
    
    # Draw foods with different shades
    for food in foods:
        shade = min(255, 100 + food[2] * 50)
        pygame.draw.rect(screen, (shade, 0, 0), [food[0], food[1], snake_block, snake_block])

    pygame.display.flip()
    clock.tick(snake_speed)

pygame.quit()