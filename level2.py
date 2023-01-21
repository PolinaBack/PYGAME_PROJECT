import time
import random
import pygame
import os
import sys


# Инициализация констант и pygame
pygame.init()
SIZE = WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode(SIZE)
text_showing = False


# функция, скачивающая и изменяющая по надобности изображения
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


# функция, отображающая сообщения и текст
def message(size, mess, color, x_mess, y_mess):
    font = pygame.font.Font(None, size)
    text_t = font.render(mess, True, color)
    SCREEN.blit(text_t, (x_mess, y_mess))


# класс машинок (красных или желтых)
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
        self.score = 4
        self.count = 0

    # функция по рандомному выбору машинок и их координат
    def driving_other_car(self, other):
        if self.rect.y < 620:
            # изменение координат
            self.rect = self.rect.move(0, self.score)
            self.count += 1
            # изменение скорости
            if self.count % 50 == 0:
                self.score += 0.5
        else:
            cy = random.randrange(-500, -150)
            cx = random.randrange(210, 489, 139)
            while cy == other.rect.y or cx == other.rect.x:
                cy = random.randrange(-500, -150)
                cx = random.randrange(210, 489, 139)
            self.rect.y = cy
            self.rect.x = cx

        if other.rect.y < 620:
            other.rect = other.rect.move(0, self.score)
        else:
            cy = random.randrange(-500, -150)
            cx = random.randrange(210, 489, 139)
            while cy == self.rect.y or cx == self.rect.x:
                cy = random.randrange(-500, -150)
                cx = random.randrange(210, 489, 139)
            other.rect.y = cy
            other.rect.x = cx


# класс Яндекс.Ровера
class Yandex_Robo_Delivery(pygame.sprite.Sprite):
    image = pygame.transform.scale(load_image('materials/models/robo-deliver.png'), (100, 130))

    def __init__(self, x, y):
        super().__init__(all_sprites)
        self.robo_delivery = Yandex_Robo_Delivery.image
        self.rect = self.robo_delivery.get_rect().move(x, y)
        self.mask = pygame.mask.from_surface(self.robo_delivery)

    # функция, отслеживающая столкновение с другими объектами
    def update(self):
        global reaction
        if pygame.sprite.collide_mask(self, other_car):
            fail_table = Fail_Menu(100, 50)
            fail_repeat = Fail_Repeat(400, 400)
            fail_main = Fail_Main(150, 405)

            SCREEN.blit(load_image('materials/images/good_background.png'), (0, 0))
            SCREEN.blit(load_image('materials/images/good_background.png'), (600, 0))
            fail.draw(SCREEN)
            clock.tick(30)  # 30 кадров в секунду
            pygame.display.flip()

            running1 = True
            while running1:
                for event1 in pygame.event.get():
                    if event1.type == pygame.QUIT:
                        running1 = False
                    if event1.type == pygame.MOUSEBUTTONDOWN:
                        if fail_main.rect.x < event1.pos[0] < fail_main.width + fail_main.rect.x and \
                                fail_main.rect.y < event1.pos[1] < fail_main.height + fail_main.rect.y:
                            from main import Menu
                            p = Menu()
                            p.main_menu()
                            running1 = False
                        if fail_repeat.rect.x < event1.pos[0] < fail_repeat.width + fail_repeat.rect.x and \
                                fail_repeat.rect.y < event1.pos[1] < fail_repeat.height + fail_repeat.rect.y:
                            import level2
                            running1 = False
            reaction = False
            time.sleep(1)

        if pygame.sprite.collide_mask(self, other_car2):
            fail_table = Fail_Menu(100, 50)
            fail_repeat = Fail_Repeat(400, 400)
            fail_main = Fail_Main(150, 405)

            SCREEN.blit(load_image('materials/images/good_background.png'), (0, 0))
            SCREEN.blit(load_image('materials/images/good_background.png'), (600, 0))
            fail.draw(SCREEN)
            clock.tick(30)  # 30 кадров в секунду
            pygame.display.flip()

            running1 = True
            while running1:
                for event1 in pygame.event.get():
                    if event1.type == pygame.QUIT:
                        running1 = False
                    if event1.type == pygame.MOUSEBUTTONDOWN:
                        if fail_main.rect.x < event1.pos[0] < fail_main.width + fail_main.rect.x and \
                                fail_main.rect.y < event1.pos[1] < fail_main.height + fail_main.rect.y:
                            from main import Menu
                            p = Menu()
                            p.main_menu()
                            running1 = False
                        if fail_repeat.rect.x < event1.pos[0] < fail_repeat.width + fail_repeat.rect.x and \
                                fail_repeat.rect.y < event1.pos[1] < fail_repeat.height + fail_repeat.rect.y:
                            import level2
                            running1 = False
            reaction = False
            time.sleep(1)

        elif self.rect.x > 490 or self.rect.x < 185:
            fail_table = Fail_Menu(100, 50)
            fail_repeat = Fail_Repeat(400, 400)
            fail_main = Fail_Main(150, 405)

            SCREEN.blit(load_image('materials/images/good_background.png'), (0, 0))
            SCREEN.blit(load_image('materials/images/good_background.png'), (600, 0))
            fail.draw(SCREEN)
            clock.tick(30)  # 30 кадров в секунду
            pygame.display.flip()

            running1 = True
            while running1:
                for event1 in pygame.event.get():
                    if event1.type == pygame.QUIT:
                        running1 = False
                    if event1.type == pygame.MOUSEBUTTONDOWN:
                        if fail_main.rect.x < event1.pos[0] < fail_main.width + fail_main.rect.x and \
                                fail_main.rect.y < event1.pos[1] < fail_main.height + fail_main.rect.y:
                            from main import Menu
                            p = Menu()
                            p.main_menu()
                            running1 = False
                        if fail_repeat.rect.x < event1.pos[0] < fail_repeat.width + fail_repeat.rect.x and \
                                fail_repeat.rect.y < event1.pos[1] < fail_repeat.height + fail_repeat.rect.y:
                            import level2
                            running1 = False
            reaction = False
            time.sleep(1)


# класс финиша
class Finish(pygame.sprite.Sprite):
    image = pygame.transform.scale(load_image('materials/images/finish2.png'), (400, 50))

    def __init__(self, x, y):
        super().__init__(all_sprites)
        self.finish = Finish.image
        self.rect = self.finish.get_rect().move(x, y)
        self.mask = pygame.mask.from_surface(self.finish)

    # функция по появлению финиша
    def moving(self, score, robot):
        global text_showing
        self.rect = self.rect.move(0, score)
        if pygame.sprite.collide_mask(self, robot):
            text_showing = True


class Comp_Menu(pygame.sprite.Sprite):
    image = load_image('materials/images/completed.png')
    image = pygame.transform.scale(image, (600, 500))

    def __init__(self, x, y):
        super().__init__(menu)
        self.cm = Comp_Menu.image
        self.rect = self.cm.get_rect().move(x, y)
        self.mask = pygame.mask.from_surface(self.cm)
        self.width = self.cm.get_width()
        self.height = self.cm.get_height()


class Fail_Menu(pygame.sprite.Sprite):
    image = load_image('materials/images/failed.png')
    image = pygame.transform.scale(image, (600, 500))

    def __init__(self, x, y):
        super().__init__(fail)
        self.cm = Fail_Menu.image
        self.rect = self.cm.get_rect().move(x, y)
        self.mask = pygame.mask.from_surface(self.cm)
        self.width = self.cm.get_width()
        self.height = self.cm.get_height()


class Comp_Next(pygame.sprite.Sprite):
    image = load_image('materials/images/comp_next.png')
    image = pygame.transform.scale(image, (150, 150))

    def __init__(self, x, y):
        super().__init__(menu)
        self.cn = Comp_Next.image
        self.rect = self.cn.get_rect().move(x, y)
        self.mask = pygame.mask.from_surface(self.cn)
        self.width = self.cn.get_width()
        self.height = self.cn.get_height()


class Comp_Back(pygame.sprite.Sprite):
    image = load_image('materials/images/comp_back.png')
    image = pygame.transform.scale(image, (150, 150))

    def __init__(self, x, y):
        super().__init__(menu)
        self.cb = Comp_Back.image
        self.rect = self.cb.get_rect().move(x, y)
        self.mask = pygame.mask.from_surface(self.cb)
        self.width = self.cb.get_width()
        self.height = self.cb.get_height()


class Comp_Main(pygame.sprite.Sprite):
    image = load_image('materials/images/comp_menu.png')
    image = pygame.transform.scale(image, (245, 125))

    def __init__(self, x, y):
        super().__init__(menu)
        self.cm = Comp_Main.image
        self.rect = self.cm.get_rect().move(x, y)
        self.mask = pygame.mask.from_surface(self.cm)
        self.width = self.cm.get_width()
        self.height = self.cm.get_height()


class Fail_Main(pygame.sprite.Sprite):
    image = load_image('materials/images/comp_menu.png')
    image = pygame.transform.scale(image, (245, 108))

    def __init__(self, x, y):
        super().__init__(fail)
        self.cm = Fail_Main.image
        self.rect = self.cm.get_rect().move(x, y)
        self.mask = pygame.mask.from_surface(self.cm)
        self.width = self.cm.get_width()
        self.height = self.cm.get_height()


class Fail_Repeat(pygame.sprite.Sprite):
    image = load_image('materials/images/repeat.png')
    image = pygame.transform.scale(image, (245, 125))

    def __init__(self, x, y):
        super().__init__(fail)
        self.cm = Fail_Main.image
        self.rect = self.cm.get_rect().move(x, y)
        self.mask = pygame.mask.from_surface(self.cm)
        self.width = self.cm.get_width()
        self.height = self.cm.get_height()

# параметры, необходимые для выполнения игры
# параметры работающие в цикле
reaction = True
x_chages, y_chages = 0, 0
x = 340
y = 445
block = 10
clock = pygame.time.Clock()
pygame.display.set_caption("Level 2")
all_sprites = pygame.sprite.Group()
menu = pygame.sprite.Group()
fail = pygame.sprite.Group()
other_car_sprite = pygame.sprite.Group()
finish = Finish(200, -100)
robot_delivery = Yandex_Robo_Delivery(x, y)
other_car = Other_Cars()
other_car2 = Other_Cars()
running = True
# основной цикл программы
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and reaction:
                x_chages -= block
            elif event.key == pygame.K_RIGHT and reaction:
                x_chages += block
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT \
                    or event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                x_chages = 0
                y_chages = 0

    robot_delivery.rect.x += x_chages
    SCREEN.fill((125, 116, 109))

    SCREEN.blit(load_image('materials/images/good_background.png'), (0, 0))
    SCREEN.blit(load_image('materials/images/good_background.png'), (600, 0))

    if other_car.score >= 13:
        finish.moving(other_car.score, robot_delivery)
    all_sprites.draw(SCREEN)
    other_car.driving_other_car(other_car2)
    font = pygame.font.Font(None, 30)
    font2 = pygame.font.Font(None, 100)
    if text_showing:
        menu_table = Comp_Menu(100, 50)
        menu_next = Comp_Next(520, 385)
        menu_back = Comp_Back(130, 375)
        menu_main = Comp_Main(282, 385)

        SCREEN.blit(load_image("materials/images/bg1.png"), (0, -200))
        menu.draw(SCREEN)
        clock.tick(30)  # 30 кадров в секунду
        pygame.display.flip()

        running1 = True
        while running1:
            for event1 in pygame.event.get():
                if event1.type == pygame.QUIT:
                    running1 = False
                if event1.type == pygame.MOUSEBUTTONDOWN:
                    if menu_next.rect.x < event1.pos[0] < menu_next.width + menu_next.rect.x and \
                            menu_next.rect.y < event1.pos[1] < menu_next.height + menu_next.rect.y:
                        import level3

                        running1 = False
                    if menu_main.rect.x < event1.pos[0] < menu_main.width + menu_main.rect.x and \
                            menu_main.rect.y < event1.pos[1] < menu_main.height + menu_main.rect.y:
                        from main import Menu

                        p = Menu()
                        p.main_menu()
                        running1 = False
                    if menu_back.rect.x < event1.pos[0] < menu_back.width + menu_back.rect.x and \
                            menu_back.rect.y < event1.pos[1] < menu_back.height + menu_back.rect.y:
                        import level1

                        running1 = False
        reaction = False
        time.sleep(1)
    all_sprites.update()
    clock.tick(30)
    pygame.display.update()
    text_t = font.render(f'score: {other_car.score}', True, (255, 0, 0))
    SCREEN.blit(text_t, (350, 10))
    pygame.display.flip()
pygame.quit()
