import time
import random
import pygame
import os
import sys

pygame.init()
SIZE = WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode(SIZE)
sp = []

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

def car(x, y):
    car1 = pygame.transform.scale(load_image('materials/models/robo-deliver.png'), (150, 150))
    SCREEN.blit(car1, (x, y))
    # pygame.display.update()

def back():
    background = load_image('materials/images/green_background1.png')
    SCREEN.blit(background, (0, 0))
    SCREEN.blit(background, (600, 0))
    # pygame.display.update()

def message(size, mess, color, x_mess, y_mess):
    font = pygame.font.Font(None, size)
    text_t = font.render(mess, True, color)
    SCREEN.blit(text_t, (x_mess, y_mess))

def crash(x):
    if x + 150 > 606 or x < 142:
        message(50, "CRASHED", (0, 0, 0), WIDTH//2 - 100, HEIGHT//2)
        time.sleep(1)

def other_car(y_en):
    car2 = pygame.transform.scale(load_image('materials/images/car2.png'), (150, 120))
    if y_en == 0:
        x_en = random.randrange(200, 467, 133)
        color_car = random.choice([(204, 6, 5), (49, 127, 67), (0, 0, 128), (232, 194, 44)])
        sp.clear()
        sp.append(x_en)
        sp.append(color_car)
    car2.fill(sp[1], special_flags=pygame.BLEND_ADD)
    SCREEN.blit(car2, (sp[0], y_en))


def main():
    y_en = 0
    x_change = 0
    lead_y = 0
    x = 300
    y = 445
    block = 10
    clock = pygame.time.Clock()
    pygame.display.set_caption('Заголовок окна')
    # all_sprites = pygame.sprite.Group()
    # место для новых спрайтов
    running = True
    while running:
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change -= block
                elif event.key == pygame.K_RIGHT:
                    x_change += block
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
        x += x_change
        SCREEN.fill((125, 116, 109))
        back()
        car(x, y)
        if y_en > 600:
            y_en = 0
        other_car(y_en)
        crash(x)

        # all_sprites.draw(SCREEN)
        # all_sprites.update()
        clock.tick(30)
        y_en += 10# 30 кадров в секунду
        pygame.display.update()
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()