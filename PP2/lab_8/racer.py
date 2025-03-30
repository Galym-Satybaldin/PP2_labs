import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Set up the display
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Racer Game")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

# Player settings
player_size = 50
player_x = width // 2
player_y = height - player_size - 10
player_speed = 5

# Enemy settings
enemy_size = 50
enemy_x = random.randint(0, width - enemy_size)
enemy_y = -enemy_size
enemy_speed = 3

# Coin settings
coin_size = 30
coins = []  # List to store multiple coins
coin_weights = [1, 2, 3]  # Different coin weights
coin_count = 0

# Game loop
clock = pygame.time.Clock()
running = True

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < width - player_size:
        player_x += player_speed

    # Move enemy
    enemy_y += enemy_speed
    if enemy_y > height:
        enemy_x = random.randint(0, width - enemy_size)
        enemy_y = -enemy_size

    # Generate random coins
    if random.randint(1, 100) < 5:  # 5% chance each frame
        coin_x = random.randint(0, width - coin_size)
        coin_weight = random.choice(coin_weights)
        coins.append([coin_x, -coin_size, coin_weight])

    # Move coins and check collision
    for coin in coins[:]:
        coin[1] += 3  # Move coin down
        # Check if player collects coin
        if (player_x < coin[0] + coin_size and
            player_x + player_size > coin[0] and
            player_y < coin[1] + coin_size and
            player_y + player_size > coin[1]):
            coin_count += coin[2]  # Add coin weight to score
            coins.remove(coin)
        # Remove coin if off screen
        elif coin[1] > height:
            coins.remove(coin)

    # Increase enemy speed every 5 coins
    enemy_speed = 3 + (coin_count // 5)

    # Draw everything
    screen.fill(BLACK)
    pygame.draw.rect(screen, RED, (player_x, player_y, player_size, player_size))  # Player
    pygame.draw.rect(screen, WHITE, (enemy_x, enemy_y, enemy_size, enemy_size))  # Enemy
    
    # Draw coins with different shades based on weight
    for coin in coins:
        shade = min(255, 100 + coin[2] * 50)  # Brighter for higher weight
        pygame.draw.circle(screen, (shade, shade, 0), (coin[0], coin[1]), coin_size // 2)

    # Display score
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Coins: {coin_count}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()