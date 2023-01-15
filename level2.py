import time
import random
import pygame
import os
import sys

pygame.init()
SIZE = WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode(SIZE)

def load_image(name, colorkey=None):
    fullname = os.path.join(name)
    if not os.path.isfile(fullname):
        print(f'Файл с изображением {fullname} не найден')
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image

def message(size, mess, color, x_mess, y_mess):
    font = pygame.font.Font(None, size)
    text_t = font.render(mess, True, color)
    SCREEN.blit(text_t, (x_mess, y_mess))

class Other_Cars(pygame.sprite.Sprite):
    im_random = random.choice(['materials/images/cool_car.png',
                               'materials/images/taxi.png'])
    image = pygame.transform.scale(load_image(im_random), (100, 150))

    def __init__(self):
        super().__init__(all_sprites)
        self.add(other_car_sprite)
        self.other_car = Other_Cars.image
        self.rect = self.other_car.get_rect().move(random.randrange(210, 489, 139), 0)
        self.mask = pygame.mask.from_surface(self.other_car)

    def driving_other_car(self, other):
        if self.rect.y < 620:
            self.rect = self.rect.move(0, 7)
        else:
            cy = random.randrange(-500, -150)
            cx = random.randrange(210, 489, 139)
            while cy == other.rect.y or cx == other.rect.x:
                cy = random.randrange(-500, -150)
                cx = random.randrange(210, 489, 139)
            self.rect.y = cy
            self.rect.x = cx

        if other.rect.y < 620:
            other.rect = other.rect.move(0, 7)
        else:
            cy = random.randrange(-500, -150)
            cx = random.randrange(210, 489, 139)
            while cy == self.rect.y or cx == self.rect.x:
                cy = random.randrange(-500, -150)
                cx = random.randrange(210, 489, 139)
            other.rect.y = cy
            other.rect.x = cx


class Yandex_Robo_Delivery(pygame.sprite.Sprite):
    image = pygame.transform.scale(load_image('materials/models/robo-deliver.png'), (120, 150))

    def __init__(self, x, y):
        super().__init__(all_sprites)
        self.robo_delivery = Yandex_Robo_Delivery.image
        self.rect = self.robo_delivery.get_rect().move(x, y)
        self.mask = pygame.mask.from_surface(self.robo_delivery)

    def update(self):
        global reaction
        if pygame.sprite.collide_mask(self, other_car):
            message(50, "CRASHED", (0, 0, 0), WIDTH // 2 - 100, HEIGHT // 2 - 25)
            self.rect.y += 7
            time.sleep(1)
            reaction = False
        if pygame.sprite.collide_mask(self, other_car2):
            message(50, "CRASHED", (0, 0, 0), WIDTH // 2 - 100, HEIGHT // 2 - 25)
            self.rect.y += 7
            reaction = False
            time.sleep(1)
        elif self.rect.x > 490 or self.rect.x < 185:
            message(50, "CRASHED", (0, 0, 0), WIDTH // 2 - 100, HEIGHT // 2 - 25)
            reaction = False
            time.sleep(1)


reaction = True
x_chages, y_chages = 0, 0
x = 340
y = 445
block = 10
clock = pygame.time.Clock()
pygame.display.set_caption('Заголовок окна')
all_sprites = pygame.sprite.Group()
other_car_sprite = pygame.sprite.Group()
robot_delivery = Yandex_Robo_Delivery(x, y)
other_car = Other_Cars()
other_car2 = Other_Cars()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and reaction:
                x_chages -= block
            elif event.key == pygame.K_RIGHT and reaction:
                x_chages += block
            elif event.key == pygame.K_UP and reaction:
                if y_chages - block + robot_delivery.rect.y > 0:
                    y_chages -= block
                else:
                    y_chages = 0
            elif event.key == pygame.K_DOWN and reaction:
                if y_chages + block + robot_delivery.rect.y + 150 < HEIGHT:
                    y_chages += block
                else:
                    y_chages = 0
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT \
                    or event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                x_chages = 0
                y_chages = 0
    robot_delivery.rect.x += x_chages
    robot_delivery.rect.y += y_chages
    SCREEN.fill((125, 116, 109))

    SCREEN.blit(load_image('materials/images/good_background.png'), (0, 0))
    SCREEN.blit(load_image('materials/images/good_background.png'), (600, 0))

    all_sprites.draw(SCREEN)
    other_car.driving_other_car(other_car2)
    all_sprites.update()
    clock.tick(30)
    pygame.display.update()
    pygame.display.flip()
pygame.quit()

