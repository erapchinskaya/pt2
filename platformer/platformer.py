import pygame
import sys
import random
from sprites.sprite_classes import *

BLACK = (0, 0, 0)
GREY = (210, 210, 210)
WIDTH = 1200
HEIGHT = 800
FPS = 60

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platformer")
clock = pygame.time.Clock()

from load import *

def restart():
    global box_group, ground_group, sand_group, \
        water_group, player_group, scroll_group, player,\
        stopEnemy_group, coin_group, enemy_group, portal_group


    box_group = pygame.sprite.Group()
    ground_group = pygame.sprite.Group()
    sand_group = pygame.sprite.Group()
    water_group = pygame.sprite.Group()
    player_group = pygame.sprite.Group()

    stopEnemy_group = pygame.sprite.Group()
    coin_group = pygame.sprite.Group()
    enemy_group = pygame.sprite.Group()
    portal_group = pygame.sprite.Group()

    scroll_group = pygame.sprite.Group()

    player = Player(player_image, (320, 560))
    player_group.add(player)



def lvlGame():
    global box_group, ground_group, sand_group, \
        water_group, player_group, scroll_group, player, \
        stopEnemy_group, coin_group, enemy_group, portal_group

    box_group.draw(window)
    ground_group.draw(window)
    sand_group.draw(window)
    water_group.draw(window)
    player_group.draw(window)

    stopEnemy_group.draw(window)
    coin_group.draw(window)
    enemy_group.draw(window)
    portal_group.draw(window)

    step = 0

    box_group.update(step, player_group, player, stopEnemy_group)
    ground_group.update(step, player_group, player, stopEnemy_group)
    sand_group.update(step, player_group, player, stopEnemy_group)
    water_group.update(step, player_group, player, stopEnemy_group)
    player_group.update(player_images, scroll_group, player_group, player, stopEnemy_group)

    stopEnemy_group.update(step, player_group, player, stopEnemy_group)
    coin_group.update(step, player_group, player, stopEnemy_group)
    enemy_group.update(step, player_group, player, stopEnemy_group)
    portal_group.update(step, player_group, player, stopEnemy_group)

    pygame.display.update()


def drawMap(mapFile):
    global box_group, ground_group, sand_group, \
        water_group, player_group, scroll_group, \
        stopEnemy_group, coin_group, enemy_group, portal_group

    game_map = []

    with open(mapFile, 'r') as file:
        for i in range(10):
            game_map.append(file.readline().replace('\n', '').split(','))

        pos = [0, 0]

        for i in range(10):
            pos[1] = i * 80
            for j in range(100):
                pos[0] = j * 80
                if game_map[i][j] == '0':
                    box = Box(box_image,(pos[0], pos[1]))
                    box_group.add(box)
                    scroll_group.add(box)
                elif game_map[i][j] == '1':
                    sand = Sand(sand_image,(pos[0], pos[1]))
                    sand_group.add(sand)
                    scroll_group.add(sand)
                elif game_map[i][j] == '2':
                    ground = Ground(ground_image,(pos[0], pos[1]))
                    ground_group.add(ground)
                    scroll_group.add(ground)
                elif game_map[i][j] == '3':
                    water = Water(water_image,(pos[0], pos[1]))
                    water_group.add(water)
                    scroll_group.add(water)
                elif game_map[i][j] == '4':
                    stop = StopEnemy(stop_image,(pos[0], pos[1]))
                    stopEnemy_group.add(stop)
                    scroll_group.add(stop)
                elif game_map[i][j] == '5':
                    coin = Coin(coin_image,(pos[0], pos[1]))
                    coin_group.add(coin)
                    scroll_group.add(coin)
                elif game_map[i][j] == '6':
                    enemy = Enemy(enemy1_image,(pos[0], pos[1]))
                    enemy_group.add(enemy)
                    scroll_group.add(enemy)
                elif game_map[i][j] == '10':
                    portal = Portal(portal_image,(pos[0], pos[1]))
                    portal_group.add(portal)
                    scroll_group.add(portal)


restart()
drawMap('game_lvl/lavel1_map.csv')


while True:

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    window.fill(GREY)

    lvlGame()