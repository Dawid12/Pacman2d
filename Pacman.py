import pygame
import Enums
from Character import Character
class Pacman(Character):
    def __init__(self, ):
        self.direction = Enums.Direction.Down
        self.mouthState = Enums.MouthState.Close
        self.x = 220
        self.y = 150
        self.imagesDict = {
            Enums.MouthState.Close: {
                    Enums.Direction.Down: pygame.image.load('data\\pl_down_2.png'),
                    Enums.Direction.Up: pygame.image.load('data\\pl_up_2.png'),
                    Enums.Direction.Left: pygame.image.load('data\\pl_left_2.png'),
                    Enums.Direction.Right: pygame.image.load('data\\pl_right_2.png')
            },
            Enums.MouthState.Open: {
                Enums.Direction.Down: pygame.image.load('data\\pl_down_1.png'),
                Enums.Direction.Up: pygame.image.load('data\\pl_up_1.png'),
                Enums.Direction.Left: pygame.image.load('data\\pl_left_1.png'),
                Enums.Direction.Right: pygame.image.load('data\\pl_right_1.png')
            }
        }
        self.surface = self.imagesDict[self.mouthState][self.direction]
        self.lifes = 3
        self.points = 0
        self.font = pygame.font.SysFont('Comic Sans MS', 30)
        return
    def getSurface(self):
        self.surface = self.imagesDict[self.mouthState][self.direction]
        return self.surface
    def getDirection(self):
        return self.direction
    def getPosition(self):
        return (self.x, self.y)
    def keepMoving(self, walls, teleports):
        move = { 'x':0, 'y':0 }
        if self.direction == Enums.Direction.Down:
            self.move(0, 1,walls, teleports)
        elif self.direction == Enums.Direction.Up:
            self.move(0, -1, walls, teleports)
        elif self.direction == Enums.Direction.Left:
            self.move(-1, 0, walls, teleports)
        elif self.direction == Enums.Direction.Right:
            self.move(1, 0, walls, teleports)
        if self.mouthState == Enums.MouthState.Close:
            self.mouthState = Enums.MouthState.Open
        else:
            self.mouthState = Enums.MouthState.Close

        return
    def move(self, xMove, yMove, walls, teleports):
        
        if self.canMove(xMove, yMove, pygame.Rect((self.x, self.y), (18,18)), walls):
            self.checkTeleports(teleports)
            self.x += xMove
            self.y += yMove
            if xMove > 0:
                self.direction = Enums.Direction.Right
            elif xMove < 0:
                self.direction = Enums.Direction.Left
            if yMove < 0:
                self.direction = Enums.Direction.Up
            elif yMove > 0:
                self.direction = Enums.Direction.Down
        return
    def checkTeleports(self, teleports):
        return
    def getPointsSurface(self):
        return self.font.render('Points: ' + str(self.points), False, (255, 0, 0))
    def getLifesSurface(self):
        return self.font.render('Lifes: ' + str(self.lifes), False, (255, 0, 0))
    def getCoordSurface(self):
        return self.font.render('X: ' + str(self.x) + ', Y: ' + str(self.y), False, (255, 150, 0))