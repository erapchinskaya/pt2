import pygame
import random

# Ball class 
class Ball(pygame.sprite.Sprite):

    def __init__(self, window, windowWidth, windowHeight):
        super().__init__()
        self.window = window  # remember the window, so we can draw later
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight

        self.image = pygame.image.load(r'assets/images/ball.png')
        self.rect = self.image.get_rect()

        self.maxWidth = windowWidth - self.rect.width
        self.maxHeight = windowHeight - self.rect.height
        
        # Pick a random starting position 
        self.rect.x = random.randrange(0, self.maxWidth)
        self.rect.y = random.randrange(0, self.maxHeight)

        # Choose a random speed between -4 and 4, but not zero
        # in both the x and y directions
        speedsList = [-4, -3, -2, -1, 1, 2, 3, 4] 
        self.xSpeed = random.choice(speedsList)
        self.ySpeed = random.choice(speedsList)

    def update(self):
        # Check for hitting a wall.  If so, change that direction.
        if self.rect.x < 0 or self.rect.x >= self.maxWidth:
            self.xSpeed = -self.xSpeed

        if self.rect.y < 0 or self.rect.y >= self.maxHeight:
            self.ySpeed = -self.ySpeed

        # Update the Ball's x and y, using the speed in two directions
        self.rect.x += self.xSpeed
        self.rect.y += self.ySpeed

    def draw(self):
        self.window.blit(self.image, self.rect)
