import pygame
import sys
from sprites.ball import Ball  

BLACK = (0, 0, 0)
WIDTH = 640
HEIGHT = 480
FPS = 60
       
pygame.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("GUI")
clock = pygame.time.Clock()  

ball = Ball(window, WIDTH, HEIGHT)

while True:

    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.time.delay(500)
            pygame.quit()
            sys.exit()          


    window.fill(BLACK)
    
    ball.draw()

    ball.update()

    pygame.display.update()


