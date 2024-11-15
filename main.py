import json

import pygame
pygame.init()

WIDTH = 800
HEIGHT = 800

game_over = 0

tile_size = 40

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
        self.width = self.image.get_width()
        self.heght = self.image.get_height()
        self.images_right = []
        self.images_left = []
        self. index = 0
        self.counter = 0
        self.direction = 0
        self.jumped = False
        self.rect.x = 100
        self.rect.y = 130
        for num in range(1, 5):
            img_right = pygame.image.load(f'images/player{num}.png')
            img_right = pygame.transform.scale(img_right, (35, 70))
            img_left = pygame.transform.flip(img_right, True, False)
            self.images_right.append(img_right)
            self.images_left.append(img_left)
        self.image = self.images_right[self.index]

    def update(self):
        global game_over
        x = 0
        y = 0
        walk_speed = 10

        if game_over == 0:
            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE] and self.jumped == False:
                self.gravity = -15
                self.jumped = True
            if key[pygame.K_LEFT]:
                x -= 5
                self.direction = -1
                self.counter += 1
            if key[pygame.K_RIGHT]:
                x += 5
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

            self.gravity += 1
            if self.gravity > 10:
                self.gravity = 10
            y += self.gravity
            for tile in world.tile_list:
                if tile[1].colliderect(self.rect.x + x, self.rect.y,
                                        self.width, self.heght):
                    x = 0
                if tile[1].colliderect(self.rect.x, self.rect.y + y,
                                       self.width, self.heght):
                    if self.gravity < 0:
                        y = tile[1].bottom - self.rect.top
                        self.gravity = 0
                    elif self.gravity >= 0:
                        y = tile[1].top - self.rect.bottom
                        self.gravity = 0
                        self.jumped = False
            if self.rect.bottom > HEIGHT:
                self.rect.bottom = HEIGHT
            self.rect.x += x
            self.rect.y += y



        elif game_over == -1:
            print('Game over')
        display.blit(self.image, self.rect)

class World:
    def __init__(self, data):
        dirt_img = pygame.image.load('tiles/dirt.png')
        grass_img = pygame.image.load("tiles/grass.png")
        self.tile_list = []
        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1 or tile == 2:
                    images = { 1: dirt_img, 2: grass_img}
                    img = pygame.transform.scale(images[tile],
                                                 (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                elif tile == 3:
                    lava = Lava(col_count * tile_size,
                                row_count * tile_size + (tile_size // 2))
                    lava_group.add(lava)
                col_count += 1
            row_count += 1
            
    def draw(self):
        for tile in self.tile_list:
            display.blit(tile[0], tile[1])

with open('./levels/level1.json', 'r') as data:

    world_data = json.load(data)
world = World(world_data)

player = Player()

class Lava(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        img = pygame.image.load('./tiles/Lava_1.png')
        self.image = pygame.transform.scale(img,
                                            (tile_size, tile_size // 2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
lava_group = pygame.sprite.Group()

run = True
while run:
    clock.tick(fps)
    display.blit(background, background_rect)
    world.draw()
    lava_group.draw(display)
    player.update()
    lava_group.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    pygame.display.update()
pygame.quit()