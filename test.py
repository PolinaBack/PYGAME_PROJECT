import pygame
import os
import sys


pygame.init()
SIZE = WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode(SIZE)
all_sprites = pygame.sprite.Group()

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


class Start_Button(pygame.sprite.Sprite):
    image = pygame.transform.scale(load_image('materials/images/start_btn.png'), (350, 100))

    def __init__(self, x, y):
        super().__init__(all_sprites)
        self.x, self.y = x, y
        self.sb = Start_Button.image
        self.rect = self.sb.get_rect().move(x, y)
        self.mask = pygame.mask.from_surface(self.sb)
        self.width = self.sb.get_width()
        self.height = self.sb.get_height()


class Choose_Button(pygame.sprite.Sprite):
    image = pygame.transform.scale(load_image('materials/images/choose_btn.png'), (350, 100))

    def __init__(self, x, y):
        super().__init__(all_sprites)
        self.x, self.y = x, y
        self.cb = Choose_Button.image
        self.rect = self.cb.get_rect().move(x, y)
        self.mask = pygame.mask.from_surface(self.cb)
        self.width = self.cb.get_width()
        self.height = self.cb.get_height()


class Rules_Button(pygame.sprite.Sprite):
    image = pygame.transform.scale(load_image('materials/images/rules_btn.png'), (350, 100))

    def __init__(self, x, y):
        super().__init__(all_sprites)
        self.x, self.y = x, y
        self.rb = Rules_Button.image
        self.rect = self.rb.get_rect().move(x, y)
        self.mask = pygame.mask.from_surface(self.rb)
        self.width = self.rb.get_width()
        self.height = self.rb.get_height()


class Back_Button(pygame.sprite.Sprite):
    image = pygame.transform.scale(load_image('materials/images/back_btn.png'), (350, 100))

    def __init__(self, x, y):
        super().__init__(back_sprite)
        self.x, self.y = x, y
        self.bb = Quit_Button.image
        self.rect = self.bb.get_rect().move(x, y)
        self.mask = pygame.mask.from_surface(self.bb)
        self.width = self.bb.get_width()
        self.height = self.bb.get_height()


class Quit_Button(pygame.sprite.Sprite):
    image = pygame.transform.scale(load_image('materials/images/quit_btn.png'), (350, 100))

    def __init__(self, x, y):
        super().__init__(all_sprites)
        self.x, self.y = x, y
        self.qb = Quit_Button.image
        self.rect = self.qb.get_rect().move(x, y)
        self.mask = pygame.mask.from_surface(self.qb)
        self.width = self.qb.get_width()
        self.height = self.qb.get_height()


class F_Lvl_Button(pygame.sprite.Sprite):
    image = pygame.transform.scale(load_image('materials/images/1_lvl_btn.png'), (200, 200))

    def __init__(self, x, y):
        super().__init__(lvl_sprites)
        self.x, self.y = x, y
        self.flb = Quit_Button.image
        self.rect = self.flb.get_rect().move(x, y)
        self.mask = pygame.mask.from_surface(self.flb)
        self.width = self.flb.get_width()
        self.height = self.flb.get_height()


class S_Lvl_Button(pygame.sprite.Sprite):
    image = pygame.transform.scale(load_image('materials/images/2_lvl_btn.png'), (200, 200))

    def __init__(self, x, y):
        super().__init__(lvl_sprites)
        self.x, self.y = x, y
        self.slb = Quit_Button.image
        self.rect = self.slb.get_rect().move(x, y)
        self.mask = pygame.mask.from_surface(self.slb)
        self.width = self.slb.get_width()
        self.height = self.slb.get_height()


class T_Lvl_Button(pygame.sprite.Sprite):
    image = pygame.transform.scale(load_image('materials/images/3_lvl_btn.png'), (200, 200))

    def __init__(self, x, y):
        super().__init__(lvl_sprites)
        self.x, self.y = x, y
        self.tlb = Quit_Button.image
        self.rect = self.tlb.get_rect().move(x, y)
        self.mask = pygame.mask.from_surface(self.tlb)
        self.width = self.tlb.get_width()
        self.height = self.tlb.get_height()

clock = pygame.time.Clock()
pygame.display.set_caption('ИГРА')
back_sprite = pygame.sprite.Group()
lvl_sprites = pygame.sprite.Group()

class Menu:
    def __init__(self):
        self.main_menu()
    def main_menu(self):
        self.start_btn = Start_Button(220, 30)
        self.choose_btn = Choose_Button(220, 150)
        self.rules_btn = Rules_Button(220, 295)
        self.quit_btn = Quit_Button(220, 440)

        SCREEN.blit(load_image("materials/images/main_bg.png"), (-300, 0))
        all_sprites.draw(SCREEN)
        all_sprites.update()
        clock.tick(30)  # 30 кадров в секунду
        pygame.display.flip()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.start_btn.rect.x < event.pos[0] < self.start_btn.width + self.start_btn.rect.x and \
                            self.start_btn.rect.y < event.pos[1] < self.start_btn.height + self.start_btn.rect.y:
                        print("ОК")

                    if self.choose_btn.rect.x < event.pos[0] < self.choose_btn.width + self.choose_btn.rect.x and \
                            self.choose_btn.rect.y < event.pos[1] < self.choose_btn.height + self.choose_btn.rect.y:
                        self.choose_level()
                        runnig = False

                    if self.rules_btn.rect.x < event.pos[0] < self.rules_btn.width + self.rules_btn.rect.x and \
                            self.rules_btn.rect.y < event.pos[1] < self.rules_btn.height + self.rules_btn.rect.y:
                        self.rules()
                        running = False

                    if self.quit_btn.rect.x < event.pos[0] < self.quit_btn.width + self.quit_btn.rect.x and \
                            self.quit_btn.rect.y < event.pos[1] < self.quit_btn.height + self.quit_btn.rect.y:
                        pygame.quit()

    def choose_level(self):
        f_lvl_btn = F_Lvl_Button(180, 50)
        s_lvl_btn = S_Lvl_Button(430, 50)
        t_lvl_btn = T_Lvl_Button(290, 300)
        SCREEN.blit(load_image("materials/images/main_bg.png"), (-300, 0))
        lvl_sprites.draw(SCREEN)
        clock.tick(30)  # 30 кадров в секунду
        pygame.display.flip()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if f_lvl_btn.rect.x < event.pos[0] < f_lvl_btn.width + f_lvl_btn.rect.x and \
                            f_lvl_btn.rect.y < event.pos[1] < f_lvl_btn.height + f_lvl_btn.rect.y:
                        self.main_menu()
                    if s_lvl_btn.rect.x < event.pos[0] < s_lvl_btn.width + s_lvl_btn.rect.x and \
                            s_lvl_btn.rect.y < event.pos[1] < s_lvl_btn.height + s_lvl_btn.rect.y:
                        self.main_menu()
                    if t_lvl_btn.rect.x < event.pos[0] < t_lvl_btn.width + t_lvl_btn.rect.x and \
                            t_lvl_btn.rect.y < event.pos[1] < t_lvl_btn.height + t_lvl_btn.rect.y:
                        self.main_menu()


    def rules(self):
        back_btn = Back_Button(430, 500)
        SCREEN.blit(load_image("materials/images/main_bg.png"), (-300, 0))
        back_sprite.draw(SCREEN)
        clock.tick(30)  # 30 кадров в секунду
        pygame.display.flip()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if back_btn.rect.x < event.pos[0] < back_btn.width + back_btn.rect.x and \
                            back_btn.rect.y < event.pos[1] < back_btn.height + back_btn.rect.y:
                        self.main_menu()



# место для новых спрайтов
    # отрисовка и изменение свойств объектов
p = Menu()
p.main_menu
pygame.quit()
