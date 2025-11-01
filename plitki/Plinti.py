import pygame
from main_r import *
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