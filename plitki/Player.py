import pygame
from main_r import *
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