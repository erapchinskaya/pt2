import pygame
import sys
from sprites.ball import Ball
from sprites.text import SimpleText
from sprites.SimpleButton import SimpleButton

# 2 - Define constants
BLACK = (0, 0, 0)
WHITE = (255,255,255)
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
ball = Ball(window, WIDTH, HEIGHT)
countLabel = SimpleText(window, (160, 20),
 'The ball was clicked: ', WHITE)
countText = SimpleText(window, (400, 20), '', WHITE)
restartButton = SimpleButton(window, (280, 60),
 r'assets/images/restartUp.png', r'assets/images/restartDown.png')
counter = 0

# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.time.delay(500)
            pygame.quit()
            sys.exit()
        if restartButton.handleEvent(event):
            counter = 0  # кнопка нажата, сбрасываем счетчик

        if event.type == pygame.MOUSEBUTTONDOWN:
            # Обрабатываем щелчок мыши
            mouse_pos = pygame.mouse.get_pos()
            if ball.rect.collidepoint(mouse_pos):
                counter += 1


    window.fill(BLACK)
    ball.draw()
    countLabel.draw()
    countText.draw()
    restartButton.draw()

    pygame.display.update()
    ball.update()
#    frameCounter = frameCounter + 1
    countText.setValue(str(counter))

    clock.tick(FPS)