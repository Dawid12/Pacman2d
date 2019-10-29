import pygame
import Enums
from Character import Character
from Move import Move
class Pacman(Character):
    def __init__(self, ):
        self.direction = Enums.Direction.Down
        self.mouthState = Enums.MouthState.Close
        self.pacmanState = Enums.PacmanState.Normal
        self.movesToNormal = 0
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
        self.previousMove = Move(0, 0)
        return
    def getSurface(self):
        self.surface = self.imagesDict[self.mouthState][self.direction]
        return self.surface
    def getDirection(self):
        return self.direction
    def getPosition(self):
        return (self.x, self.y)
    def move(self, move, walls, teleports, coins, scares, ghosts):
        if self.canMove(move, pygame.Rect((self.x, self.y), (18,18)), walls):
            teleport = self.recognizeTeleport(move, pygame.Rect((self.x, self.y), (18,18)), teleports)
            if teleport != None:
                if teleport.left == 0:
                    self.makeMove(Move(500, 0), Enums.Direction.Left)
                else:
                    self.makeMove(Move(-500, 0), Enums.Direction.Right)
            else:
                self.makeMove(move, None)
        else:
            if self.canMove(self.previousMove, pygame.Rect((self.x, self.y), (18,18)), walls):
                self.makeMove(self.previousMove, None)
        if self.movesToNormal > 0:
            self.movesToNormal -= 1
            if self.movesToNormal < 1:
                self.pacmanState = Enums.PacmanState.Normal
                self.movesToNormal = 0
        self.checkForCoins(coins)
        self.checkForScares(scares)
        self.checkForGhosts(ghosts)
        self.handleMouth()
        return
    def makeMove(self, move, direction):
        self.previousMove = move
        self.x += move.x
        self.y += move.y
        if direction == None:
            if move.x > 0:
                self.direction = Enums.Direction.Right
            elif move.x < 0:
                self.direction = Enums.Direction.Left
            if move.y < 0:
                self.direction = Enums.Direction.Up
            elif move.y > 0:
                self.direction = Enums.Direction.Down
        else:
            self.direction = direction
        return
    def checkForCoins(self, coins):
        actualRect = pygame.Rect((self.x, self.y), (18,18))
        for coin in coins:
            if coin.colliderect(actualRect):
                coins.remove(coin)
                self.points += 1
                break
        return
    def checkForScares(self, scares):
        actualRect = pygame.Rect((self.x, self.y), (18,18))
        for scare in scares:
            if scare.colliderect(actualRect):
                scares.remove(scare)
                self.pacmanState = Enums.PacmanState.OnSteroids
                self.movesToNormal = 900
        return
    def checkForGhosts(self, ghosts):
        actualRect = pygame.Rect((self.x, self.y), (18,18))
        for ghost in ghosts:
            if ghost.getRect().colliderect(actualRect):
                if self.pacmanState == Enums.PacmanState.Normal:
                    #death
                    print("jur ded")
                elif self.pacmanState == Enums.PacmanState.OnSteroids:
                    self.points += 100
                    ghost.setState(Enums.GhostState.Eaten)
        return
    def handleMouth(self):
        if self.mouthState == Enums.MouthState.Close:
            self.mouthState = Enums.MouthState.Open
        else:
            self.mouthState = Enums.MouthState.Close
    def draw(self, screen):
        screen.blit(self.getSurface(), self.getPosition())
        screen.blit(self.getPointsSurface(), (0,0))
        screen.blit(self.getLifesSurface(), (200,0))
        screen.blit(self.getCoordSurface(), (0, 670))
        return
    def getPointsSurface(self):
        return self.font.render('Points: ' + str(self.points), False, (255, 0, 0))
    def getLifesSurface(self):
        return self.font.render('Lifes: ' + str(self.lifes), False, (255, 0, 0))
    def getCoordSurface(self):
        return self.font.render('X: ' + str(self.x) + ', Y: ' + str(self.y), False, (255, 150, 0))
    def getPacmanState(self):
        return self.pacmanState