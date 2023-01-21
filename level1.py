import random
from collections import Counter
import pygame
import os
import sys

# Инициализация констант и pygame
pygame.init()
clock = pygame.time.Clock()
SIZE = WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode(SIZE)

# создание списка, для вывода списка продуктов
mess = []
font = pygame.font.Font(None, 30)
x_mess = 10
# рандомный выбор озвучки заказа
choice1 = random.choice(["materials/audios/order1.wav", "materials/audios/order2.wav"])
if choice1 == "materials/audios/order2.wav":
    correct_check = ['Цезарь Ролл-----1', 'Куриные наггетсы-----1', 'Кофе----2', 'Пирожок с вишней----3', 'Пирожок с яблоком----3']
else:
    correct_check = ['Картофель Фри----3', 'Куриные наггетсы-----1', 'Биг Мак----2', 'Кока-Кола----3']
sound_1 = pygame.mixer.Sound(choice1)

# установка заднего фона
bg = pygame.image.load("materials/images/bg1.png")
SCREEN.blit(bg, (0, 0))
pygame.display.flip()


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


# класс Картофеля Фри
class Fries_Potato(pygame.sprite.Sprite):
    image = pygame.transform.scale(load_image('materials/models/fries.png'), (130, 130))

    def __init__(self, x, y):
        super().__init__(all_sprites)
        self.x, self.y = x, y
        self.fries = Fries_Potato.image
        self.rect = self.fries.get_rect().move(x, y)
        self.mask = pygame.mask.from_surface(self.fries)
        self.width = self.fries.get_width()
        self.height = self.fries.get_height()


# класс Кофе
class Coffee_c(pygame.sprite.Sprite):
    image = pygame.transform.scale(load_image('materials/models/coffe.png'), (100, 140))

    def __init__(self, x, y):
        super().__init__(all_sprites)
        self.x, self.y = x, y
        self.coffee = Coffee_c.image
        self.rect = self.coffee.get_rect().move(x, y)
        self.mask = pygame.mask.from_surface(self.coffee)
        self.width = self.coffee.get_width()
        self.height = self.coffee.get_height()


# класс Яблочного пирожка
class Apple_Pie_a(pygame.sprite.Sprite):
    image = pygame.transform.scale(load_image('materials/models/apple pie.png'), (162, 120))

    def __init__(self, x, y):
        super().__init__(all_sprites)
        self.x, self.y = x, y
        self.apple = Apple_Pie_a.image
        self.rect = self.apple.get_rect().move(x, y)
        self.mask = pygame.mask.from_surface(self.apple)
        self.width = self.apple.get_width()
        self.height = self.apple.get_height()


# класс БигМака
class BigMac(pygame.sprite.Sprite):
    image = pygame.transform.scale(load_image('materials/models/bigmac.png'), (166, 120))

    def __init__(self, x, y):
        super().__init__(all_sprites)
        self.x, self.y = x, y
        self.bigmac = BigMac.image
        self.rect = self.bigmac.get_rect().move(x, y)
        self.mask = pygame.mask.from_surface(self.bigmac)
        self.width = self.bigmac.get_width()
        self.height = self.bigmac.get_height()


# класс Цезарь Ролла
class Cezar_Roll_c(pygame.sprite.Sprite):
    image = pygame.transform.scale(load_image('materials/models/cezar roll.png'), (126, 189))

    def __init__(self, x, y):
        super().__init__(all_sprites)
        self.x, self.y = x, y
        self.cezar_roll = Cezar_Roll_c.image
        self.rect = self.cezar_roll.get_rect().move(x, y)
        self.mask = pygame.mask.from_surface(self.cezar_roll)
        self.width = self.cezar_roll.get_width()
        self.height = self.cezar_roll.get_height()


# класс Вишневого пирожка
class Cherry_Pie_c(pygame.sprite.Sprite):
    image = pygame.transform.scale(load_image('materials/models/cherry pie.png'), (162, 120))

    def __init__(self, x, y):
        super().__init__(all_sprites)
        self.x, self.y = x, y
        self.cherry_pie = Cherry_Pie_c.image
        self.rect = self.cherry_pie.get_rect().move(x, y)
        self.mask = pygame.mask.from_surface(self.cherry_pie)
        self.width = self.cherry_pie.get_width()
        self.height = self.cherry_pie.get_height()


# класс Кока-колы
class Coca_cola_c(pygame.sprite.Sprite):
    image = pygame.transform.scale(load_image('materials/models/cola.png'), (140, 140))

    def __init__(self, x, y):
        super().__init__(all_sprites)
        self.x, self.y = x, y
        self.coca_cola = Coca_cola_c.image
        self.rect = self.coca_cola.get_rect().move(x, y)
        self.mask = pygame.mask.from_surface(self.coca_cola)
        self.width = self.coca_cola.get_width()
        self.height = self.coca_cola.get_height()


# класс Наггетсов
class Nuggets_n(pygame.sprite.Sprite):
    image = pygame.transform.scale(load_image('materials/models/nuggets.png'), (132, 120))

    def __init__(self, x, y):
        super().__init__(all_sprites)
        self.x, self.y = x, y
        self.nuggets = Nuggets_n.image
        self.rect = self.nuggets.get_rect().move(x, y)
        self.mask = pygame.mask.from_surface(self.nuggets)
        self.width = self.nuggets.get_width()
        self.height = self.nuggets.get_height()


# класс анимации говорящего человечка
class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y):
        super().__init__(all_sprites)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.count = 2

    # функция разделения картинок
    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    # функция смены картинок и звука
    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]
        if self.count % 2 == 0:
            sound_1.set_volume(20)
            sound_1.play()
        else:
            sound_1.stop()
        self.count += 1


# класс Яндекс.Ровера
class Yandex_Robo_Delivery2(pygame.sprite.Sprite):
    image = pygame.transform.scale(load_image('materials/models/robo-deliver.png'), (220, 250))

    def __init__(self, x, y):
        super().__init__(all_sprites)
        self.robo_delivery = Yandex_Robo_Delivery2.image
        self.rect = self.robo_delivery.get_rect().move(x, y)
        self.mask = pygame.mask.from_surface(self.robo_delivery)
        self.width = self.robo_delivery.get_width()
        self.height = self.robo_delivery.get_height()
        self.mess = []
        self.trash = []

    # функция реакции по попытке добавления продуктов в робо-станцию
    # и обновления списка добавленных продуктов
    def update(self, other_obg):
        other_obg.rect.x, other_obg.rect.y = other_obg.x, other_obg.y
        if all_objects[other_obg] not in self.trash:
            self.trash.append(all_objects[other_obg])
            self.mess.append(all_objects[other_obg] + '1')
        else:
            position = self.trash.index(all_objects[other_obg])
            c = all_objects[other_obg][:-1] + str(int(self.mess[position][-1]) + 1)
            del self.mess[position]
            self.mess.insert(position, c)


class Error_end(pygame.sprite.Sprite):
    image = load_image('materials/images/end_level1.png')
    image = pygame.transform.scale(image, (150, 80))

    def __init__(self, x, y):
        super().__init__(all_sprites)
        self.stop_end = Error_end.image
        self.rect = self.stop_end.get_rect().move(x, y)
        self.mask = pygame.mask.from_surface(self.stop_end)
        self.width = self.stop_end.get_width()
        self.height = self.stop_end.get_height()


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


class Check_order(pygame.sprite.Sprite):
    image = load_image('materials/images/check_level1.png')
    image = pygame.transform.scale(image, (150, 80))

    def __init__(self, x, y):
        super().__init__(all_sprites)
        self.check_end = Check_order.image
        self.rect = self.check_end.get_rect().move(x, y)
        self.mask = pygame.mask.from_surface(self.check_end)
        self.width = self.check_end.get_width()
        self.height = self.check_end.get_height()


# параметры, необходимые для выполнения игры
# параметры работающие в цикле
running = True
rect_go = False
x_pos, y_pos = 0, 0
pygame.display.set_caption("Level 1")
all_sprites = pygame.sprite.Group()
menu = pygame.sprite.Group()
all_objects = {}
n = 0
count = 0
# создание объектов классов
robot_delivery = Yandex_Robo_Delivery2(250, 345)
stop = Error_end(10, 500)
check = Check_order(630, 500)
men = AnimatedSprite(pygame.transform.scale(load_image("materials/images/anima_men2.png"), (350, 250)), 2, 1, 490, 320)
coffee_d = Coffee_c(160, 0)
all_objects[coffee_d] = 'Кофе-----'
fries_p = Fries_Potato(10, 0)
all_objects[fries_p] = 'Картофель Фри-----'
apple_pie = Apple_Pie_a(300, 0)
all_objects[apple_pie] = 'Пирожок с яблоком-----'
big_mac = BigMac(150, 170)
all_objects[big_mac] = 'Биг Мак-----'
cezar_roll = Cezar_Roll_c(330, 140)
all_objects[cezar_roll] = 'Цезарь Ролл-----'
cherry_pie = Cherry_Pie_c(610, 0)
all_objects[cherry_pie] = 'Пирожок с вишней-----'
coca_cola = Coca_cola_c(470, 0)
all_objects[coca_cola] = 'Кока-Кола-----'
nuggets = Nuggets_n(480, 170)
all_objects[nuggets] = 'Куриные наггетсы-----'


def compare(x, y):
    return Counter(x) == Counter(y)


# основной цикл программы
while running:
    SCREEN.blit(load_image("materials/images/bg1.png"), (0, -200))
    all_sprites.draw(SCREEN)
    y_mess = 340
    for m in mess:
        text_t = font.render(m, True, (0, 0, 0))
        SCREEN.blit(text_t, (x_mess, y_mess))
        y_mess += 20
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # воспроизведение заказа
            if men.rect.x < event.pos[0] < men.width + men.rect.x and \
                    men.rect.y < event.pos[1] < men.height + men.rect.y:
                men.update()
        for obg in all_objects:
            if event.type == pygame.MOUSEBUTTONDOWN:
                # печать заказа слева
                if stop.rect.x < event.pos[0] < stop.width + stop.rect.x and \
                        stop.rect.y < event.pos[1] < stop.height + stop.rect.y:
                    mess = []
                    robot_delivery.mess = []
                    robot_delivery.trash = []
                # Провека на переход к следущему уровню
                if check.rect.x < event.pos[0] < check.width + check.rect.x and \
                        check.rect.y < event.pos[1] < check.height + check.rect.y:
                    # сделать переход на некст уровень
                    if compare(correct_check, mess):
                        menu_table = Comp_Menu(100, 50)
                        menu_next = Comp_Next(520, 385)
                        menu_back = Comp_Back(130, 375)
                        menu_main = Comp_Main(282, 385)

                        SCREEN.blit(load_image("materials/images/bg1.png"), (0, -200))
                        menu.draw(SCREEN)
                        clock.tick(30)
                        pygame.display.flip()
                        running1 = True
                        while running1:
                            for event1 in pygame.event.get():
                                if event1.type == pygame.QUIT:
                                    running1 = False
                                if event1.type == pygame.MOUSEBUTTONDOWN:
                                    if menu_next.rect.x < event1.pos[0] < menu_next.width + menu_next.rect.x and \
                                            menu_next.rect.y < event1.pos[1] < menu_next.height + menu_next.rect.y:
                                        import level2
                                        running1 = False
                                    if menu_main.rect.x < event1.pos[0] < menu_main.width + menu_main.rect.x and \
                                            menu_main.rect.y < event1.pos[1] < menu_main.height + menu_main.rect.y:
                                        from main import Menu
                                        p = Menu()
                                        p.main_menu()
                                        running1 = False
                        running = False
                if obg.rect.x < event.pos[0] < obg.rect.x + obg.width \
                        and obg.rect.y < event.pos[1] < obg.rect.y + obg.height:
                    rect_go = True
                    n = obg
            # перемещение продукта в робо-станцию
            if event.type == pygame.MOUSEMOTION and rect_go and obg == n:
                n.rect.x, n.rect.y = n.rect.x + event.rel[0], n.rect.y + event.rel[1]
            if event.type == pygame.MOUSEBUTTONUP and obg == n:
                if robot_delivery.rect.x < n.rect.x < robot_delivery.width + robot_delivery.rect.x and \
                        robot_delivery.rect.y < n.rect.y < robot_delivery.height + robot_delivery.rect.y:
                    robot_delivery.update(n)
                    mess = robot_delivery.mess
                rect_go = False
    pygame.display.flip()

pygame.quit()
