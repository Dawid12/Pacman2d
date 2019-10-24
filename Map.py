import pygame
import Enums
class Map:
    def __init__(self, path):
        self.mapPath = path
        self.elementWidth = 20
        self.elementHeight = 20
        self.walls = []
        self.coins = []
        self.passages = []
        self.doors = []
        self.teleports = []
        self.imagesDict = {
            Enums.MapElement.Wall: pygame.image.load('data\\wall.png'),
            Enums.MapElement.Passage: pygame.image.load('data\\passage.png'),
            Enums.MapElement.Coin: pygame.image.load('data\\gold.png'),
            Enums.MapElement.Door: pygame.image.load('data\\door.png')
        }
        return
    def getMap(self):
        x = 0
        y = 50
        with open(self.mapPath, 'r') as mapFile:
            for line in mapFile:
                for element in line:
                    if element == '\n':
                        break
                    if element == Enums.MapElement.Wall.value:
                        self.walls.append(pygame.Rect((x, y), (self.elementWidth, self.elementHeight)))
                    elif element == Enums.MapElement.Coin.value:
                        self.coins.append(pygame.Rect((x, y), (self.elementWidth, self.elementHeight)))
                    elif element == Enums.MapElement.Passage.value:
                        self.passages.append(pygame.Rect((x, y), (self.elementWidth, self.elementHeight)))
                    elif element == Enums.MapElement.Door.value:
                        self.doors.append(pygame.Rect((x, y), (self.elementWidth, self.elementHeight)))
                    elif element == Enums.MapElement.Teleport.value:
                        self.teleports.append(pygame.Rect((x, y), (self.elementWidth, self.elementHeight)))
                    x += self.elementWidth
                x = 0
                y += self.elementHeight

    def drawWalls(self, screen):
        for wall in self.walls:
            screen.blit(self.imagesDict[Enums.MapElement.Wall], (wall.left, wall.top))
    def drawPassages(self, screen):
        for passage in self.passages:
            screen.blit(self.imagesDict[Enums.MapElement.Passage], (passage.left, passage.top))
    def drawCoins(self, screen):
        for coin in self.coins:
            screen.blit(self.imagesDict[Enums.MapElement.Coin], (coin.left, coin.top))
    def drawDoors(self, screen):
        for door in self.doors:
            screen.blit(self.imagesDict[Enums.MapElement.Door], (door.left, door.top))
    def drawTeleports(self, screen):
        for teleport in self.teleports:
            screen.blit(self.imagesDict[Enums.MapElement.Passage], (teleport.left, teleport.top))
    def getWalls(self):
        return self.walls
    def getTeleports(self):
        return self.teleports
