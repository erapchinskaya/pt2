import pygame
import sys
from sprites.ball import Ball
from sprites.text import SimpleText
from sprites.SimpleButton import SimpleButton
from pygwidgets import *

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
click_sound = pygame.mixer.Sound(r'assets/sounds/click.mp3')
# 5 - Initialize variables
background = pygwidgets.Image(window, (0, 0), r'assets/images/background.jpg')
ball = Ball(window, WIDTH, HEIGHT)
countLabel = SimpleText(window, (160, 20),
 'The ball was clicked: ', WHITE)
countText = SimpleText(window, (400, 20), '', WHITE)
restartButton = SimpleButton(window, (500, 420),
 r'assets/images/restartUp.png', r'assets/images/restartDown.png')

button1 = pygwidgets.TextButton(window, (500, 370), 'Нажми')

textA = pygwidgets.DisplayText(window, (20, 50), 'Текст 1',
                                    fontSize=36, textColor=WHITE)

textB = pygwidgets.DisplayText(window, (20, 150),
                                       'Строка 1\nСтрока 2\nСтрока 3',
                                       fontSize=36, textColor=WHITE, justified='center')

inputA = pygwidgets.InputText(window, (20, 350), '',
                                  fontSize=30, textColor=BLACK, backgroundColor=WHITE)

inputB= pygwidgets.InputText(window, (20, 430), '', width = 400,
                                  fontSize=30, textColor=WHITE, backgroundColor=BLACK)
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
                click_sound.play()

        if  button1.handleEvent(event):
                print('Кнопка была нажата')

        if inputA.handleEvent(event):
            userText = inputA.getText()
            print('В первое поле ввода пользователь ввел:', userText)

        if inputB.handleEvent(event):
            userText = inputB.getText()
            print('Во второе поле ввода пользователь ввел:', userText)


    window.fill(BLACK)
    background.draw()
    ball.draw()
    countLabel.draw()
    countText.draw()
    restartButton.draw()
    button1.draw()
    textA.draw()
    textB.draw()
    inputA.draw()
    inputB.draw()

    pygame.display.update()
    ball.update()
#    frameCounter = frameCounter + 1
    countText.setValue(str(counter))

    clock.tick(FPS)