import pygame
pygame.init()


class Paddle:

    def __init__(self, X, Y):
        self.paddle = pygame.Rect(X, Y, 20, 100)

    def displayPaddle(self, surface):
        pygame.draw.rect(surface, (255, 255, 255), self.paddle, 10, 3)

    def getPaddleAsRect(self):
        return self.paddle

    def moveRightPaddle(self):
        pressedKeys = pygame.key.get_pressed()
        if pressedKeys[pygame.K_UP]:
            self.paddle.y -= 2
        if pressedKeys[pygame.K_DOWN]:
            self.paddle.y += 2

    def moveLeftPaddle(self):
        pressedKeys = pygame.key.get_pressed()
        if pressedKeys[pygame.K_w]:
            self.paddle.y -= 2
        if pressedKeys[pygame.K_s]:
            self.paddle.y += 2

    def checkPaddlePosition(self, surfaceH):
        if self.paddle.y < 0:
            self.paddle.y = 0
        if self.paddle.y > surfaceH - 100:
            self.paddle.y = surfaceH - 100
