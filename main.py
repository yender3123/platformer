import pygame
pygame.init()

WIDTH = 800
HEIGHT = 800

clock = pygame.time.Clock()
fps = 60

display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Platformer')



background = pygame.image.load('background/bg1.png')
background_rect = background.get_rect()

class Player:
    def __init__(self):
        self.image = pygame.image.load('images/player1.png')
        self.image = pygame.transform.scale(self.image, (50, 70))
        self.rect = self.image.get_rect()
        self.gravity = 0

        self.jumped = False
        self.rect.x = 100
        self.rect.y = 130

    def update(self):
        x = 0
        y = 0
        walk_speed = 10
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and self.jumped == False:
            self.gravity = -15
            self.jumped = True
        if key[pygame.K_LEFT]:
            x -= 5
            self.direction = -1
            self.counter += 1
        if key[pygame.K_RIGHT]:
            x -= 5
            self.direction = 1
            self.counter += 1

        if self.counter > walk_speed:
            self.counter = 0
            self.gravity += 1
            if self.index >= len(self.images_right):
                self.index = 0
            if self.direction == 1:
                self.image = self.images_right[self.index]
            else:
                self.image = self.images_left[self.index]

        if self.gravity > 10:
            self.gravity = 10
        y += self.gravity
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        self.rect.x += x
        self.rect.y += y
        display.blit(self.image, self.rect)

player = Player()

run = True
while run:
    clock.tick(fps)
    display.blit(background, background_rect)

    player.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    pygame.display.update()
pygame.quit()