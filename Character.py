import pygame
from Move import Move
class Character:
    def __int__(self):
        self.rect = None
        self.direction = None
        self.surface = None
    def canMove(self, move, actualRect, walls):
        afterMove = actualRect.move((move.x, move.y))
        for wall in walls:
            if wall.colliderect(afterMove):
                return False
        return True
    def recognizeTeleport(self, move, actualRect, teleports):
        afterMove = actualRect.move((move.x, move.y))
        for teleport in teleports:
            if teleport.colliderect(afterMove):
                return teleport
        return None