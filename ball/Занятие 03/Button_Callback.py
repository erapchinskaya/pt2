import pygame
from pygame.locals import *
from sprites.SimpleButton import *
import sys

# 2 - Define constants
GRAY = (200, 200, 200)
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 100
FRAMES_PER_SECOND = 30


# Define a function to be used as a "callback"
def myCallBackFunction():
    print('User pressed Button B, called myCallBackFunction')


# Define a class with a method to be used as a "callback"
class CallBackClass():
    def __init__(self):
        pass

    def myMethod(self):
        print('User pressed Button C, called myMethod of the CallBackTest object')


# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Load assets: image(s), sounds, etc.

# 5 - Initialize variables

myCallBack = CallBackClass()
# Create instances of SimpleButton
# No call back
buttonA = SimpleButton(window, (25, 30),
                        r'assets/images/buttonAUp.png',
                        r'assets/images/buttonADown.png')
# Specifying a function to call back
buttonB = SimpleButton(window, (150, 30),
                        r'assets/images/buttonBUp.png',
                        r'assets/images/buttonBDown.png',
                        callBack=myCallBackFunction)
# Specifying method to call back
buttonC = SimpleButton(window, (275, 30),
                        r'assets/images/buttonCUp.png',
                        r'assets/images/buttonCDown.png',
                        callBack=myCallBack.myMethod)
counter = 0

# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Pass the event to the button, see if has been clicked on
        if buttonA.handleEvent(event):
            print('User pressed button A, handled in the main loop')

        # oButtonB and oButtonC have callbacks,
        # no need to check result of these calls
        buttonB.handleEvent(event)

        buttonC.handleEvent(event)

    # 8 - Do any "per frame" actions
    counter = counter + 1

    # 9 - Clear the window
    window.fill(GRAY)

    # 10 - Draw all window elements
    buttonA.draw()
    buttonB.draw()
    buttonC.draw()

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait
