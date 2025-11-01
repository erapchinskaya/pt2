import pygame
import sys
from pygwidgets import *
import random

# 2 - Define constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WIDTH = 640
HEIGHT = 480
FPS = 60

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rock. Scissors. Paper")
clock = pygame.time.Clock()

# 4 - Load assets: image(s), sounds, etc.

# 5 - Initialize variables
scoreAI = 0
scoreU = 0
choiceAI = ''
choiceU = ''
textScoreAI = pygwidgets.DisplayText(window, (50, 50), f'AI Score: {scoreAI}',
                                    fontSize=36, textColor=BLACK)
textScoreU = pygwidgets.DisplayText(window, (350, 50), f'User Score: {scoreU}',
                                    fontSize=36, textColor=BLACK)
imgAI = pygwidgets.Image(window, (50, 100), r'images/RSP.jpg')
imgU = pygwidgets.Image(window, (350, 100), r'images/RSP.jpg')

labelAI = pygwidgets.DisplayText(window, (50, 300), f'AI Choice: {choiceAI}',
                                    fontSize=36, textColor=BLACK)
labelU = pygwidgets.DisplayText(window, (350, 300), f'User Choice: {choiceU}',
                                    fontSize=36, textColor=BLACK)
labelWin = pygwidgets.DisplayText(window, (350, 300), f'You win',
                                    fontSize=36, textColor=BLACK)
labelInput = pygwidgets.DisplayText(window, (120, 420), 'Enter your choice',
                                    fontSize=26, textColor=BLACK)
inputU = pygwidgets.InputText(window, (270, 420), '',
                                  fontSize=30, textColor=WHITE, backgroundColor=BLACK)
# 6 - Loop forever
while True:

    clock.tick(FPS)

    # 7 - Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if inputU.handleEvent(event):
            userText = inputU.getText()

            # 8 - Do any "per frame" actions

    # 9 - Clear the window before drawing it again
    window.fill(WHITE)

    # 10 - Draw the window elements
    textScoreAI.draw()
    textScoreU.draw()
    imgAI.draw()
    imgU.draw()
    labelAI.draw()
    labelU.draw()
    labelInput.draw()
    inputU.draw()
    # 11 - Update the window
    pygame.display.update()
