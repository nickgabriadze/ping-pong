import pygame
from Ball import Ball
from Paddle import Paddle

pygame.init()
pygame.display.set_caption("Ping Pong")


class PingPong:
    __WIDTH = 720
    __HEIGHT = 500
    __FPS = 60

    def __init__(self) -> None:
        self.__running = True
        self.__clock = pygame.time.Clock()
        self.__display = pygame.display.set_mode((self.__WIDTH, self.__HEIGHT))
        self.ball = Ball(self.__WIDTH // 2 - 30, self.__HEIGHT // 2 - 30)
        self.leftPaddle = Paddle(10, self.__HEIGHT // 2 - 30)
        self.rightPaddle = Paddle(self.__WIDTH - 40, self.__HEIGHT // 2 - 30)
        self.gameOver = False

    def startGame(self) -> None:

        while self.__running:
            self.__clock.tick(self.__FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__running = False

            self.__display.fill(10)
            self.gameEventBlocks()
            self.endGame()
            pygame.display.flip()

    def gameEventBlocks(self):
        self.leftPaddle.displayPaddle(self.__display)
        self.rightPaddle.displayPaddle(self.__display)
        self.leftPaddle.moveLeftPaddle()
        self.rightPaddle.moveRightPaddle()

        self.ball.drawBall(self.__display)

        # self.ball.dropBall()
        self.ball.ballKeepMoving()

        self.gameOver = self.ball.checkBorders(self.__WIDTH, self.__HEIGHT)
        self.ball.checkForPaddleCollision(self.leftPaddle, self.rightPaddle,
                                          self.__WIDTH)
        self.leftPaddle.checkPaddlePosition(self.__HEIGHT)
        self.rightPaddle.checkPaddlePosition(self.__HEIGHT)

    def returnDisplayHeight(self):
        return self.__HEIGHT

    def endGame(self):
        if self.gameOver[0]:
            self.displayGameOverText()

    def displayGameOverText(self):
        if self.gameOver[2] is None:
            whoWon = "None of the Paddles Won"
            placement = 250
        elif self.gameOver[1]:
            whoWon = "Left Paddle Won"
            placement = 170
        else:
            whoWon = "Right paddle Won"
            placement = 180

        gameOverFont = pygame.font.Font("Picture and Font/BungeeShade-Regular.ttf", 30)
        gameOverText = gameOverFont.render(whoWon, False, (255, 255, 255))
        self.__display.blit(gameOverText, (self.__WIDTH // 2 - placement, self.__HEIGHT // 2 - 40))


if __name__ == "__main__":
    pingPong = PingPong()
    pingPong.startGame()
