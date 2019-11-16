from Character import Character
from Move import Move
import math
import Enums
import random
import pygame
class Ghost(Character):
    def __init__(self, imageDict, type, x, y):
        self.image = imageDict[type]
        self.imageDict = imageDict
        self.type = type
        self.x = x
        self.y = y
        self.state = Enums.GhostState.Normal
        self.pacmanFindingThreshold = 200
    def setRect(self, rect):
        self.rect = rect
    def getRect(self):
        return pygame.Rect((self.x, self.y), (18,18))
    def getImage(self):
        if self.state == Enums.GhostState.Normal:
            self.image = self.imageDict[self.type]
        elif self.state == Enums.GhostState.Eaten:
            self.image = self.imageDict[Enums.MapElement.Eaten]
        elif self.state == Enums.GhostState.Frightened:
            self.image = self.imageDict[Enums.MapElement.Frightened]
        return self.image
    def getCoords(self):
        return (self.x, self.y)
    def setState(self, state):
        self.state = state
    def getState(self):
        return self.state
    def makeMove(self, move):
        self.x += move.x
        self.y += move.y
        return
    def makeRandomMove(self, move, walls, teleports):
        moveDirection = list(range(1,5))
        random.shuffle(moveDirection)
        for direction in moveDirection:
            move = Move.initWithDirection(Enums.Direction(direction))
            if self.canMove(move, pygame.Rect((self.x, self.y), (18,18)), walls):
                teleport = self.recognizeTeleport(move, pygame.Rect((self.x, self.y), (18,18)), teleports)
                if teleport != None:
                    if teleport.left == 0:
                        self.makeMove(Move(500, 0))
                    else:
                        self.makeMove(Move(-500, 0))
                else:
                    self.makeMove(move)

                break;
        return
    def isPacmanNear(self, pacmanCoords):
        x,y = pacmanCoords
        xDistance = self.x - x
        yDistance = self.y - y
        distance = math.sqrt(xDistance*xDistance + yDistance*yDistance)
        if distance < self.pacmanFindingThreshold:
            return True
        return False
    def getDirectionTowardsPacman(self, pacmanCoords):
        x,y = pacmanCoords
        if self.x - x > 0:
            return Enums.Direction.Left
        elif x - self.x > 0:
            return Enums.Direction.Right
        elif self.y - y > 0:
            return Enums.Direction.Up
        elif y - self.y > 0:
            return Enums.Direction.Down
        else:
            return None
    def moveInDirection(self, direction, walls, teleports):
        move = Move.initWithDirection(Enums.Direction(direction))
        if self.canMove(move, pygame.Rect((self.x, self.y), (18,18)), walls):
            teleport = self.recognizeTeleport(move, pygame.Rect((self.x, self.y), (18,18)), teleports)
            if teleport != None:
                if teleport.left == 0:
                    self.makeMove(Move(500, 0))
                else:
                    self.makeMove(Move(-500, 0))
            else:
                self.makeMove(move)
        else:
            self.makeRandomMove(move, walls, teleports)
        return
