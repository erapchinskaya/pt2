import pygame
import sys
from pygwidgets import *
import random

# 2 - Define constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (200, 200, 200)
WIDTH = 640
HEIGHT = 480
FPS = 60

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rock. Scissors. Paper")
clock = pygame.time.Clock()

# 4 - Load assets: image(s), sounds, etc.
IMAGES = {
    'rock': r'images/rock.png',
    'scissors': r'images/scissors.png',
    'paper': r'images/paper.png',
    'default': r'images/RSP.jpg'
}

# 5 - Initialize variables
def restart(arg):
    global scoreU, scoreAI, choiceU, choiceAI, resultText, imgU, imgAI
    scoreAI = 0
    scoreU = 0
    choiceAI = ''
    choiceU = ''
    resultText = ''
    imgAI = pygwidgets.Image(window, (50, 100), IMAGES['default'])
    imgU = pygwidgets.Image(window, (350, 100), IMAGES['default'])

scoreAI = 0
scoreU = 0
choiceAI = ''
choiceU = ''
resultText = ''

textScoreAI = pygwidgets.DisplayText(window, (50, 50), f'AI Score: {scoreAI}',
                                        fontSize=36, textColor=BLACK)
textScoreU = pygwidgets.DisplayText(window, (350, 50), f'User Score: {scoreU}',
                                    fontSize=36, textColor=BLACK)
imgAI = pygwidgets.Image(window, (50, 100), IMAGES['default'])
imgU = pygwidgets.Image(window, (350, 100), IMAGES['default'])

labelAI = pygwidgets.DisplayText(window, (50, 320), f'AI Choice: {choiceAI}',
                                    fontSize=30, textColor=BLACK)
labelU = pygwidgets.DisplayText(window, (350, 320), f'User Choice: {choiceU}',
                                    fontSize=30, textColor=BLACK)
labelResult = pygwidgets.DisplayText(window, (220, 360), resultText,
                                    fontSize=36, textColor=BLACK)

labelInput = pygwidgets.DisplayText(window, (120, 420), 'Enter your choice:',
                                    fontSize=26, textColor=BLACK)
inputU = pygwidgets.InputText(window, (300, 415), '',
                                  fontSize=30, textColor=BLACK, backgroundColor=GREY)

buttonRestart = pygwidgets.TextButton(window, (520, 410), 'restart', width=80, height=40, callBack=restart)



# 6 - Main loop
while True:
    clock.tick(FPS)

    # 7 - Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        buttonRestart.handleEvent(event)

        if inputU.handleEvent(event):
            userText = inputU.getText().strip().lower()

            if userText in ['rock', 'scissors', 'paper']:
                choiceU = userText
                choiceAI = random.choice(['rock', 'scissors', 'paper'])

                # Обновляем картинки
                imgAI = pygwidgets.Image(window, (50, 100), IMAGES[choiceAI])
                imgU = pygwidgets.Image(window, (350, 100), IMAGES[choiceU])
                # imgU.setImage(IMAGES[choiceU])
                # imgAI.setImage(IMAGES[choiceAI])

                # Определяем победителя
                if choiceU == choiceAI:
                    resultText = "It's a draw!"
                elif (choiceU == 'rock' and choiceAI == 'scissors') or \
                     (choiceU == 'scissors' and choiceAI == 'paper') or \
                     (choiceU == 'paper' and choiceAI == 'rock'):
                    resultText = "You win!"
                    scoreU += 1
                else:
                    resultText = "AI wins!"
                    scoreAI += 1



                # Обновляем текстовые элементы
                textScoreAI.setValue(f'AI Score: {scoreAI}')
                textScoreU.setValue(f'User Score: {scoreU}')
                labelAI.setValue(f'AI Choice: {choiceAI}')
                labelU.setValue(f'User Choice: {choiceU}')
                labelResult.setValue(resultText)

                # Очищаем поле ввода
                inputU.setValue('')
            else:
                labelResult.setValue("Invalid input! Use rock, scissors, or paper.")
                inputU.setValue('')

    # 9 - Clear window
    window.fill(WHITE)

    # 10 - Draw everything
    textScoreAI.draw()
    textScoreU.draw()
    imgAI.draw()
    imgU.draw()
    labelAI.draw()
    labelU.draw()
    labelResult.draw()
    labelInput.draw()
    inputU.draw()
    buttonRestart.draw()

    # 11 - Update window
    pygame.display.update()