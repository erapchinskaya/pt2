import pygame
import os
import sys

current_path = os.path.dirname(__file__)
os.chdir(current_path)
pygame.init()
WIDTH = 1000
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
clock = pygame.time.Clock()

on_image = pygame.image.load('data/images/on.png').convert_alpha()
of_image = pygame.image.load('data/images/of.png').convert_alpha()
p_1_image = pygame.image.load('data/images/p_1.png').convert_alpha()
p_2_image = pygame.image.load('data/images/p_2.png').convert_alpha()

plitka_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()

list_player = []
NUM_HOD = 0
font = pygame.font.SysFont('Arial', 40)

maps_list = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
]


def game():
    screen.fill('grey')
    plitka_group.update()
    plitka_group.draw(screen)
    player_group.update()
    player_group.draw(screen)
    if len(player_group) == 1:
        text = f'win player: {list_player[0].name}'
    else:
        text = f'Ход игрока {list_player[NUM_HOD].name}'
    tt = font.render(text, True, 'black')
    screen.blit(tt, (720, 10))
    pygame.display.update()


class Plitka(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = on_image
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.on = True
        self.adr = (self.rect.y // 100, self.rect.x // 100)

    def update(self):
        if pygame.sprite.spritecollide(self, player_group, False):
            self.on = False
            self.image = of_image
            maps_list[self.adr[0]][self.adr[1]] = 1

        pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:
            if self.on:
                if self.rect.left < pos[0] < self.rect.right and self.rect.top < pos[1] < self.rect.bottom:
                    list_player[NUM_HOD].step = True


class Player(pygame.sprite.Sprite):
    def __init__(self, image, x, y, name):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.hod = False  # активен ли ход игрок -
        self.step = False  # сделал ли игрок ход
        self.name = name

    def update(self):
        global NUM_HOD
        if self.hod:
            if not self.proverka():  # self.proverka () функция которая проверяет, есть ли у игрока ходы
                NUM_HOD += 1
                if NUM_HOD > len(list_player) - 1:
                    NUM_HOD = 0
                list_player[NUM_HOD].hod = True
                list_player.remove(self)
                self.kill()
                return
            if pygame.mouse.get_pressed()[0]:
                if self.step:

                    click_pos = pygame.mouse.get_pos()
                    if ((click_pos[0] - self.rect.centerx) ** 2 +
                        (click_pos[1] - self.rect.centery) ** 2) ** 0.5 <= 150:
                        self.rect.x = 10 + click_pos[0] // 100 * 100
                        self.rect.y = 10 + click_pos[1] // 100 * 100
                        self.step = False
                        NUM_HOD += 1
                        if NUM_HOD > len(list_player) - 1:
                            NUM_HOD = 0
                        list_player[NUM_HOD].hod = True
                        self.hod = False

    def proverka(self):

        pl_c = pygame.sprite.spritecollide(self, plitka_group, False)
        if not pl_c:
            return False

        pl = pl_c[0]
        x = pl.adr[1]
        y = pl.adr[0]

        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                index_y = y + i
                index_x = x + j
                if 0 <= index_x < 7 and 0 <= index_y < 7:
                    if maps_list[index_y][index_x] == 0:
                        return True

        return False


def drawmaps():
    for i in range(0, 7):
        for j in range(0, 7):
            x = 100 * i
            y = 100 * j
            pos = (x, y)
            plitka = Plitka(pos)
            plitka_group.add(plitka)


player_1 = Player(p_1_image, 10, 10, 'Andrei')
player_group.add(player_1)
list_player.append(player_1)
player_2 = Player(p_2_image, 610, 610, 'Sasha')
player_group.add(player_2)
list_player.append(player_2)
list_player[0].hod = True

drawmaps()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    clock.tick(FPS)

    game()
