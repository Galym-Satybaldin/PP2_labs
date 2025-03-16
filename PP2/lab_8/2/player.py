import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Simple Music Player")

background = pygame.image.load('MRdrake.jpg')
background = pygame.transform.scale(background, (400, 300))

songs = ['GP.mp3', 'RF.mp3']
current_song = 0

pygame.mixer.music.load(songs[current_song])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                pygame.mixer.music.play()
            if event.key == pygame.K_s:
                pygame.mixer.music.stop()
            if event.key == pygame.K_n:
                current_song = (current_song + 1) % len(songs)
                pygame.mixer.music.load(songs[current_song])
                pygame.mixer.music.play()
            if event.key == pygame.K_b:
                current_song = (current_song - 1) % len(songs)
                pygame.mixer.music.load(songs[current_song])
                pygame.mixer.music.play()

    screen.blit(background, (0, 0))
    pygame.display.flip()
