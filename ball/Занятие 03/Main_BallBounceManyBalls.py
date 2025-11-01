# pygame demo 6(b) - using the Ball class, bounce many balls

# 1 - Import packages
import sys
from sprites.ball import *  # bring in the Ball class code

# 2 - Define constants
BLACK = (0, 0, 0)
WIDTH = 640
HEIGHT = 480
FPS = 60
N_BALLS = 3

# 3 - Initialize the world
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("GUI")
clock = pygame.time.Clock()
ballGroup = pygame.sprite.Group()
for i in range(0, N_BALLS):
    ball = Ball(screen, WIDTH, HEIGHT)
    ballGroup.add(ball)  # append the new Ball to the list of Balls
ingame = True
while ingame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.time.delay(500)
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Обрабатываем щелчок мыши
            mouse_pos = pygame.mouse.get_pos()
            for sprite in ballGroup:
                if sprite.rect.collidepoint(mouse_pos):
                    sprite.kill()
            if len(ballGroup) == 0:
                ingame = False
    ballGroup.update()  # tell each Ball to update itself
    screen.fill(BLACK)
    ballGroup.draw(screen)   # tell each Ball to draw itself
    pygame.display.update()
    clock.tick(FPS)  # make pygame wait

pygame.time.delay(500)
pygame.quit()
sys.exit()
