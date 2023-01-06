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
    im_random = random.choice(['materials/images/blue_car.png', 'materials/images/green_car.png',
                               'materials/images/red_car.jpg'])
    image = pygame.transform.scale(load_image('materials/images/car2.png'), (150, 120))

    def __init__(self):
        super().__init__(all_sprites)
        self.add(other_car_sprite)
        self.other_car = Other_Cars.image
        self.rect = self.other_car.get_rect().move(random.randrange(200, 467, 133), 0)
        self.color_car = random.choice([(204, 6, 5), (49, 127, 67), (0, 0, 128), (232, 194, 44)])
        self.other_car.fill(self.color_car, special_flags=pygame.BLEND_ADD)
        self.mask = pygame.mask.from_surface(self.other_car)

    def driving_other_car(self, other):
        if self.rect.y < 620:
            self.rect = self.rect.move(0, 7)
        else:
            cy = random.randrange(-500, -120)
            cx = random.randrange(200, 467, 133)
            while cy == other.rect.y or cx == other.rect.x:
                cy = random.randrange(-500, -120)
                cx = random.randrange(200, 467, 133)
            self.rect.y = cy
            self.rect.x = cx

            # self.other_car = Other_Cars.image
            #
            # self.color_car = random.choice([(204, 6, 5), (49, 127, 67), (0, 0, 128), (232, 194, 44)])
            # self.other_car.fill(self.color_car, special_flags=pygame.BLEND_ADD)
        if other.rect.y < 620:
            other.rect = other.rect.move(0, 7)
        else:
            cy = random.randrange(-500, -120)
            cx = random.randrange(200, 467, 133)
            while cy == self.rect.y or cx == self.rect.x:
                cy = random.randrange(-500, -120)
                cx = random.randrange(200, 467, 133)
            other.rect.y = cy
            other.rect.x = cx

            # other.other_car = Other_Cars.image

            # other.color_car = random.choice([(204, 6, 5), (49, 127, 67), (0, 0, 128), (232, 194, 44)])
            # other.other_car.fill(other.color_car, special_flags=pygame.BLEND_ADD)
            # self.color_car = random.choice([(204, 6, 5), (49, 127, 67), (0, 0, 128), (232, 194, 44)])



class Yandex_Robo_Delivery(pygame.sprite.Sprite):
    image = pygame.transform.scale(load_image('materials/models/robo-deliver.png'), (150, 150))

    def __init__(self, x, y):
        super().__init__(all_sprites)
        self.robo_delivery = Yandex_Robo_Delivery.image
        self.rect = self.robo_delivery.get_rect().move(x, y)
        self.mask = pygame.mask.from_surface(self.robo_delivery)

    def update(self):
        if pygame.sprite.collide_mask(self, other_car):
            message(50, "CRASHED", (0, 0, 0), WIDTH // 2 - 100, HEIGHT // 2 - 25)
            self.rect.y += 7
            time.sleep(1)
        if pygame.sprite.collide_mask(self, other_car2):
            message(50, "CRASHED", (0, 0, 0), WIDTH // 2 - 100, HEIGHT // 2 - 25)
            self.rect.y += 7
            time.sleep(1)
        elif self.rect.x > 450 or self.rect.x < 200:
            message(50, "CRASHED", (0, 0, 0), WIDTH // 2 - 100, HEIGHT // 2 - 25)



y_en = 0
lead_y = 0
x_chages = 0
x = 300
y = 445
block = 10
clock = pygame.time.Clock()
pygame.display.set_caption('Заголовок окна')
all_sprites = pygame.sprite.Group()
other_car_sprite = pygame.sprite.Group()
robot_delivery = Yandex_Robo_Delivery(x, y)
other_car = Other_Cars()
other_car2 = Other_Cars()
# место для новых спрайтов
running = True
while running:
    for event in pygame.event.get():
        # при закрытии окна
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_chages -= block
            elif event.key == pygame.K_RIGHT:
                x_chages += block
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_chages = 0
    robot_delivery.rect.x += x_chages
    # print(robot_delivery.rect.x)
    # x += robot_delivery.rect.x
    # print(x)
    SCREEN.fill((125, 116, 109))

    # back()
    # car(x, y)
    # if y_en > 600:
    #     y_en = 0
    # other_car(y_en)
    # crash(x)
    SCREEN.blit(load_image('materials/images/good_background.png'), (0, 0))
    SCREEN.blit(load_image('materials/images/good_background.png'), (600, 0))

    all_sprites.draw(SCREEN)
    # other_car2.driving_other_car()
    other_car.driving_other_car(other_car2)
    all_sprites.update()
    clock.tick(30)# 30 кадров в секунду
    pygame.display.update()
    pygame.display.flip()
pygame.quit()

