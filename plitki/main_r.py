import pygame
import os
import sys
from Player import Player
from Plinti import *

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
