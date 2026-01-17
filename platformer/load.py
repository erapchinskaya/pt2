import pygame

player_image = pygame.image.load('images/player.png').convert_alpha()
player_images = {'right': player_image,
                 'left': pygame.transform.flip(player_image, True, False)}

box_image = pygame.image.load('images/blocks/box.png').convert_alpha()
sand_image = pygame.image.load('images/blocks/center.png').convert_alpha()
ground_image = pygame.image.load('images/blocks/earth.png').convert_alpha()
water_image = pygame.image.load('images/blocks/water.png').convert_alpha()
stop_image = pygame.image.load('images/blocks/stop.png').convert_alpha()

enemy1_image = pygame.image.load('images/enemy/1/1.png').convert_alpha()
enemy2_image = pygame.image.load('images/enemy/2/1.png').convert_alpha()
enemy3_image = pygame.image.load('images/enemy/3/1.png').convert_alpha()

portal_image = pygame.image.load('images/portal/Portal_100x100px1.png').convert_alpha()

coin_image = pygame.image.load('images/item/monetka.png').convert_alpha()