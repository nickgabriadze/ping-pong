import pygame


class Ball:
    __image = pygame.transform.scale(pygame.image.load("Picture and Font/Ball.png"), (30, 30))
    __moveDirection = True  # in this case True is indicating positive direction
    __gameJustStarted = None
    __ballSpeedX = 3
    __ballSpeedY = 1.5

    def __init__(self, X, Y):
        self.ball = self.__image.get_rect(topleft=[X, Y])
        self.__dropBall = False

    def drawBall(self, surface):
        surface.blit(self.__image, (self.ball.x, self.ball.y))

    def ballKeepMoving(self):
        self.ball.x += self.__ballSpeedX
        self.ball.y += self.__ballSpeedY
        self.checkUpperAndLowerBorders()

    def checkUpperAndLowerBorders(self):
        if self.ball.y < 0 or self.ball.y > 470:
            self.__ballSpeedY *= -1

    def checkBorders(self, surfaceW, surfaceH):
        if self.ball.x > surfaceW + 30 or self.ball.x < -30 or \
                self.ball.y > surfaceH + 30 or self.ball.y < -30:
            return [True, self.__moveDirection, self.__gameJustStarted]

        return [False, None]

    def getPosition(self):
        return [self.ball.x, self.ball.y]

    def checkForPaddleCollision(self, leftPaddle, rightPaddle, surfaceW):
        if self.ball.colliderect(leftPaddle.getPaddleAsRect()) \
                or self.ball.colliderect(rightPaddle.getPaddleAsRect()):
            self.__gameJustStarted = False

            if self.ball.x < surfaceW // 2:
                self.__moveDirection = True
                self.__ballSpeedX *= -1
                self.ballKeepMoving()

            if self.ball.x > surfaceW // 2:
                self.__ballSpeedX *= -1
                self.__moveDirection = False

                self.ballKeepMoving()

    def getBallAsRect(self):
        return self.ball
