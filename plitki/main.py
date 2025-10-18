import pygame
import os
import sys

current_path = os.path.dirname(__file__)
os.chdir(current_path)
pygame.init()
WIDTH = 1000
HEIGHT = 800
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

on_image = pygame.image.load('data/images/on.png').convert_alpha()
of_image = pygame.image.load('data/images/of.png').convert_alpha()
p_1_image = pygame.image.load('data/images/p_1.png').convert_alpha()
p_2_image = pygame.image.load('data/images/p_2.png').convert_alpha()

plitka_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
list_player = []
NUM_HOD = 0
font = pygame.font.SysFont('Aria', 40)

maps_list = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
]


class Plitka(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = on_image  # картинка плитки
        self.rect = self.image.get_rect()  # Хитбокс плитки
        self.rect.topleft = pos  # положение плитки указывается при ее сосдании
        self.on = True  # можно ли наступить на плитку
        self.adr = (self.rect.y // 100, self.rect.x // 100)
        # адрес плитки в maps_list


def drawmaps():
    for i in range(0, 7):
        for j in range(0, 7):
            x = 100 * i
            y = 100 * j
            pos = (x, y)
            plitka = Plitka(pos)
            plitka_group.add(plitka)


def game():
    screen.fill('grey')
    plitka_group.update()
    plitka_group.draw(screen)
    player_group.update()
    player_group.draw(screen)
    pygame.display.update()


drawmaps()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    clock.tick(FPS)
    game()
