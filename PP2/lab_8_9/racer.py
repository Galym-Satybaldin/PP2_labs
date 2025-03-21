import pygame
import random

pygame.init()

# Screen setup
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game")

# Colors
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Player properties
player_width = 40
player_height = 60
player_x = WIDTH // 2
player_y = HEIGHT - 100
player_speed = 5  # Lateral movement speed

# Enemy properties
enemy_width = 40
enemy_height = 60
enemies = []
base_enemy_speed = 4

# Coin properties
coin_size = 20
coins = []
coin_count = 0
base_coin_speed = 3

# Game velocity multiplier
velocity_multiplier = 1.0  # Starts at normal speed
max_multiplier = 2.0  # Caps at double speed

def spawn_coin():
    # Spawn coins at random x position
    x = random.randint(0, WIDTH - coin_size)
    coins.append([x, -coin_size])

def spawn_enemy():
    # Spawn enemies at random x position
    x = random.randint(0, WIDTH - enemy_width)
    enemies.append([x, -enemy_height])

def update_velocity_multiplier(coins_collected):
    # Gradually increase velocity based on coins, capped at max_multiplier
    new_multiplier = 1.0 + (coins_collected * 0.1)  # 10% speed increase per coin
    return min(new_multiplier, max_multiplier)

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
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed

    # Update velocity multiplier based on coins
    velocity_multiplier = update_velocity_multiplier(coin_count)

    # Coin spawning (2% chance each frame)
    if random.random() < 0.02:
        spawn_coin()

    # Enemy spawning (1% chance each frame)
    if random.random() < 0.01:
        spawn_enemy()

    # Update coins
    for coin in coins[:]:
        coin[1] += base_coin_speed * velocity_multiplier  # Move coin down with increasing speed
        # Check collision with player
        if (player_x < coin[0] + coin_size and 
            player_x + player_width > coin[0] and
            player_y < coin[1] + coin_size and
            player_y + player_height > coin[1]):
            coins.remove(coin)
            coin_count += 1
        # Remove coins that go off screen
        elif coin[1] > HEIGHT:
            coins.remove(coin)

    # Update enemies
    for enemy in enemies[:]:
        enemy[1] += base_enemy_speed * velocity_multiplier  # Move enemy down with increasing speed
        # Check collision with player
        if (player_x < enemy[0] + enemy_width and 
            player_x + player_width > enemy[0] and
            player_y < enemy[1] + enemy_height and
            player_y + player_height > enemy[1]):
            running = False  # End game on collision
        # Remove enemies that go off screen
        elif enemy[1] > HEIGHT:
            enemies.remove(enemy)

    # Drawing
    screen.fill((0, 0, 0))  # Black background
    
    # Draw player
    pygame.draw.rect(screen, RED, (player_x, player_y, player_width, player_height))
    
    # Draw coins
    for coin in coins:
        pygame.draw.circle(screen, YELLOW, (coin[0], coin[1]), coin_size // 2)
    
    # Draw enemies
    for enemy in enemies:
        pygame.draw.rect(screen, BLUE, (enemy[0], enemy[1], enemy_width, enemy_height))
    
    # Draw score and velocity
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Coins: {coin_count}", True, WHITE)
    velocity_text = font.render(f"Velocity: {velocity_multiplier:.1f}x", True, WHITE)
    screen.blit(score_text, (WIDTH - 150, 10))
    screen.blit(velocity_text, (WIDTH - 150, 50))

    pygame.display.flip()
    clock.tick(60)

# Game over message
font = pygame.font.Font(None, 74)
game_over_text = font.render("Game Over!", True, WHITE)
screen.blit(game_over_text, (WIDTH//2 - 150, HEIGHT//2 - 50))
pygame.display.flip()
pygame.time.wait(2000)  # Show game over for 2 seconds

pygame.quit()