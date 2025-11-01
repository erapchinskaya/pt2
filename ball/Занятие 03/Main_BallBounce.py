# pygame demo 6(a) - using the Ball class, bounce one ball

# 1 - Import packages
import sys
from sprites.ball import *  # bring in the Ball class code

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
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()          
    ball.update()  # tell the Ball to update itself
    window.fill(BLACK)
    ball.draw()   # tell the Ball to draw itself
    pygame.display.update()
    clock.tick(FPS)  # make pygame wait


