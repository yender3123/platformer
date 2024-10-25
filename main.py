import pygame
pygame.init()

WIDTH = 800
HEIGHT = 800

display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Platformer')

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()