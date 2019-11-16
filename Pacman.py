import pygame
import Enums
import time
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
            },
            Enums.MouthState.ClosedForever: {
                1: pygame.image.load('data\\death1.png'),
                2: pygame.image.load('data\\death2.png'),
                3: pygame.image.load('data\\death3.png'),
                4: pygame.image.load('data\\death4.png'),
                5: pygame.image.load('data\\death5.png'),
                6: pygame.image.load('data\\death6.png'),
                7: pygame.image.load('data\\death7.png'),
                8: pygame.image.load('data\\death8.png'),
                9: pygame.image.load('data\\death9.png'),
                10: pygame.image.load('data\\death10.png'),
                11: pygame.image.load('data\\death11.png'),
            }
        }
        self.surface = self.imagesDict[self.mouthState][self.direction]
        self.lifes = 3
        self.points = 0
        self.font = pygame.font.SysFont('Comic Sans MS', 30)
        self.previousMove = Move(0, 0)
        self.death = False
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
                    self.death = True
                elif self.pacmanState == Enums.PacmanState.OnSteroids:
                    if ghost.getState() == Enums.GhostState.Frightened:
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

    def reset(self):
        self.direction = Enums.Direction.Down
        self.mouthState = Enums.MouthState.Close
        self.pacmanState = Enums.PacmanState.Normal
        self.movesToNormal = 0
        self.x = 220
        self.y = 150
        self.previousMove = Move(0, 0)
        return

    def isDead(self):
        return self.death

    def pacmanDeath(self, screen):
        for death in self.imagesDict[Enums.MouthState.ClosedForever]:
            image = self.imagesDict[Enums.MouthState.ClosedForever][death]
            screen.blit(image, self.getPosition())
            pygame.display.flip()
            time.sleep(0.2)

    def gameOver(self, screen):
        text = self.font.render("Game Over!", False, (231, 254, 0))
        screen.blit(text, (200,360))
        pygame.display.flip()
        time.sleep(2)

    def handleDeath(self, screen):
        self.death = False
        self.pacmanDeath(screen)
        self.reset()
        if self.lifes == 0:
            self.gameOver(screen)
            return False
        elif self.lifes > 0:
            self.lifes -= 1
            return True