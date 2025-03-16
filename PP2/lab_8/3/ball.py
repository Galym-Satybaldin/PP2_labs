import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Moving Red Ball")

ball_pos = [200, 200]
ball_radius = 25
move_distance = 20

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and ball_pos[1] - ball_radius - move_distance >= 0:
                ball_pos[1] -= move_distance
            if event.key == pygame.K_DOWN and ball_pos[1] + ball_radius + move_distance <= 400:
                ball_pos[1] += move_distance
            if event.key == pygame.K_LEFT and ball_pos[0] - ball_radius - move_distance >= 0:
                ball_pos[0] -= move_distance
            if event.key == pygame.K_RIGHT and ball_pos[0] + ball_radius + move_distance <= 400:
                ball_pos[0] += move_distance

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), ball_pos, ball_radius)
    pygame.display.flip()