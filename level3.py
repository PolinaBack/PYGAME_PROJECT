import time
import pygame
import os
import sys

pygame.init()
SIZE = WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Level 3")

FPS = 50
clock = pygame.time.Clock()
player = None
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
font = pygame.font.Font(None, 30)
texting_show = False


def load_image(name, color_key=None):
    fullname = os.path.join(name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


def load_level(filename):
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    max_width = max(map(len, level_map))
    return [line.ljust(max_width, '.') for line in level_map]

tile_images = {
    'wall': pygame.transform.scale(load_image('materials/images/box.png'), (80, 80)),
    'empty': pygame.transform.scale(load_image('materials/images/tales2.jpg'), (80, 80)),
    'bush': pygame.transform.scale(load_image('materials/images/bush.png'), (80, 80)),
    'lake': pygame.transform.scale(load_image('materials/images/lake_picture.png'), (80, 80)),
    'finish': pygame.transform.scale(load_image('materials/images/finish.png'), (80, 80))
}
player_image = pygame.transform.scale(load_image('materials/models/robo-deliver.png'), (60, 60))
tile_width = tile_height = 80


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        print(pos_x * tile_width)
        print()
        print(pos_y * tile_height)
        self.rect = self.image.get_rect().move(pos_x * tile_width, pos_y * tile_height)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.image = player_image
        self.rect = self.image.get_rect().move(pos_x * tile_width + 2, pos_y * tile_height + 2)

    def wall_crash(self, col_obj):
        global texting_show, time_out
        if pygame.sprite.collide_rect(self, col_obj) and col_obj.image == tile_images['wall']\
                and (button == 'right' or button == 'left'):
            player.rect.x -= x_chages
        elif pygame.sprite.collide_rect(self, col_obj) and col_obj.image == tile_images['wall']\
                and (button == 'up' or button == 'down'):
            player.rect.y -= y_chages
        # if pygame.sprite.collide_rect(self, col_obj) and col_obj.image == tile_images['bush'] \
        #         and (button == 'right' or button == 'left'):
        #     player.image.set_alpha(150)
        if pygame.sprite.collide_rect(self, col_obj) and col_obj.image == tile_images['bush']:
            player.image.set_alpha(150)
        if pygame.sprite.collide_rect(self, col_obj) and col_obj.image == tile_images['lake'] \
                and (button == 'right' or button == 'left'):
            player.rect.x -= x_chages
        elif pygame.sprite.collide_rect(self, col_obj) and col_obj.image == tile_images['lake'] \
                and (button == 'up' or button == 'down'):
            player.rect.y -= y_chages
        if pygame.sprite.collide_rect(self, col_obj) and col_obj.image == tile_images['finish']:
            texting_show = True
            time_out = time.time()
            text_t = font.render(f'fINiSH', True, (0, 0, 0))
            SCREEN.blit(text_t, (350, 10))


def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                # print(x, y)
                Tile('empty', x, y)
            elif level[y][x] == '@':
                Tile('empty', x, y)
                new_player = Player(x, y)
            elif level[y][x] == '#':
                Tile('wall', x, y)
            elif level[y][x] == '*':
                Tile('bush', x, y)
            elif level[y][x] == '~':
                Tile('lake', x, y)
            elif level[y][x] == '$':
                Tile('finish', x, y)
    return new_player, x, y

player, level_x, level_y = generate_level(load_level("materials/data/level3.txt"))


class Camera:
    def __init__(self):
        self.dx = 0
        self.dy = 0
    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy
    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - WIDTH // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - HEIGHT // 2)


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


camera = Camera()
menu = pygame.sprite.Group()
running = True
x_chages, y_chages = 0, 0
reaction = True
time_go = False
block = 5
button = ''
# Главный Игровой цикл
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if not time_go:
                now = time.time()
            time_go = True
            if event.key == pygame.K_LEFT and reaction:
                x_chages -= block
                button = 'left'
                player.image = pygame.transform.rotate(player_image, 90)
            elif event.key == pygame.K_RIGHT and reaction:
                x_chages += block
                button = 'right'
                player.image = pygame.transform.rotate(player_image, 270)
            elif event.key == pygame.K_UP and reaction:
                # if y_chages - block + player.rect.y > 0:
                y_chages -= block
                button = 'up'
                player.image = pygame.transform.rotate(player_image, 0)
                # else:
                #     y_chages = 0
            elif event.key == pygame.K_DOWN and reaction:
                # if y_chages + block + player.rect.y + 150 < HEIGHT:
                y_chages += block
                button = 'down'
                player.image = pygame.transform.rotate(player_image, 180)
                # else:
                #     y_chages = 0
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT \
                    or event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                x_chages = 0
                y_chages = 0
    player.rect.x += x_chages
    player.rect.y += y_chages
    camera.update(player)
    for sprite in all_sprites:
        player.wall_crash(sprite)
        camera.apply(sprite)
    SCREEN.fill(pygame.Color(127, 199, 255))
    tiles_group.draw(SCREEN)
    player_group.draw(SCREEN)
    if time_go:
        text_t = font.render(f'{round((time.time() - now), 1)}', True, (255, 255, 255))
        SCREEN.blit(text_t, (350, 10))
    if texting_show:
        menu_table = Comp_Menu(100, 50)
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
                    if menu_main.rect.x < event1.pos[0] < menu_main.width + menu_main.rect.x and \
                            menu_main.rect.y < event1.pos[1] < menu_main.height + menu_main.rect.y:
                        from test import Menu

                        p = Menu()
                        p.main_menu()
                        running1 = False
        running = False

    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()
sys.exit()
