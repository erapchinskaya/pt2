# 1 - Import packages
import pygame
import sys
from sprites.ball import *  # bring in the Ball class code

# 2 - Define constants
BLACK = (0, 0, 0)
WIDTH = 640
HEIGHT = 480
FPS = 60

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("GUI")
clock = pygame.time.Clock()

# 4 - Load assets: image(s), sounds, etc.

# 5 - Initialize variables

# 6 - Loop forever
while True:

    clock.tick(FPS)

    # 7 - Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

            # 8 - Do any "per frame" actions

    # 9 - Clear the window before drawing it again
    window.fill(BLACK)

    # 10 - Draw the window elements

    # 11 - Update the window
    pygame.display.update()
