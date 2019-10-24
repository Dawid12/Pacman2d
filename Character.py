import pygame

class Character:
    def __int__(self):
        self.rect = None
        self.direction = None
        self.surface = None
    def canMove(self, x, y, actualRect, walls):
        afterMove = actualRect.move((x, y))
        for wall in walls:
            if wall.colliderect(afterMove):
                return False
        return True
