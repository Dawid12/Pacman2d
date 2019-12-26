import pygame
import Enums
from Ghost import Ghost
from Pacman import Pacman
class Map:
    def __init__(self, path):
        self.fruitSpawned = False
        self.font = pygame.font.SysFont('Comic Sans MS', 30)
        self.mapPath = path
        self.elementWidth = 20
        self.elementHeight = 20
        self.fruits = []
        self.walls = []
        self.coins = []
        self.passages = []
        self.doors = []
        self.teleports = []
        self.scares = []
        self.ghosts = []
        self.imagesDict = {
            Enums.MapElement.Wall: pygame.image.load('data\\wall.png'),
            Enums.MapElement.Passage: pygame.image.load('data\\passage.png'),
            Enums.MapElement.Coin: pygame.image.load('data\\gold.png'),
            Enums.MapElement.Door: pygame.image.load('data\\door.png'),
            Enums.MapElement.Scare: pygame.image.load('data\\scare.png'),
            Enums.MapElement.GhostBlue: pygame.image.load('data\\blue.png'),
            Enums.MapElement.GhostPink: pygame.image.load('data\\pink.png'),
            Enums.MapElement.GhostRed: pygame.image.load('data\\red.png'),
            Enums.MapElement.GhostOrange: pygame.image.load('data\\orange.png'),
            Enums.MapElement.Frightened: pygame.image.load('data\\frightened.png'),
            Enums.MapElement.Eaten: pygame.image.load('data\\eaten.png'),
            Enums.MapElement.Fruit: pygame.image.load('data\\fruit.png')
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
                    elif element == Enums.MapElement.Scare.value:
                        self.scares.append(pygame.Rect((x, y), (self.elementWidth, self.elementHeight)))
                    elif element == Enums.MapElement.GhostRed.value or element == Enums.MapElement.GhostPink.value or element == Enums.MapElement.GhostBlue.value or element == Enums.MapElement.GhostOrange.value:
                        enumElement = Enums.MapElement(element)
                        ghost = Ghost(self.imagesDict, enumElement, x, y)
                        ghost.setRect(pygame.Rect((x, y), (self.elementWidth, self.elementHeight)))
                        self.ghosts.append(ghost)
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
    def drawFruits(self, screen):
        for fruit in self.fruits:
            screen.blit(self.imagesDict[Enums.MapElement.Fruit], (fruit.left, fruit.top))
    def drawDoors(self, screen):
        for door in self.doors:
            screen.blit(self.imagesDict[Enums.MapElement.Door], (door.left, door.top))
    def drawTeleports(self, screen):
        for teleport in self.teleports:
            screen.blit(self.imagesDict[Enums.MapElement.Passage], (teleport.left, teleport.top))
    def drawScares(self, screen):
        for scare in self.scares:
            screen.blit(self.imagesDict[Enums.MapElement.Scare], (scare.left, scare.top))
    def drawGhosts(self, screen, pacmanState):
        for ghost in self.ghosts:
            if pacmanState == Enums.PacmanState.OnSteroids and ghost.getState() == Enums.GhostState.Normal:
                ghost.setState(Enums.GhostState.Frightened)
            elif pacmanState == Enums.PacmanState.Normal and (ghost.getState() == Enums.GhostState.Frightened or ghost.getState() == Enums.GhostState.Eaten):
                ghost.setState(Enums.GhostState.Normal)
            screen.blit(ghost.getImage(), ghost.getCoords())
    def getWalls(self):
        return self.walls
    def getTeleports(self):
        return self.teleports
    def getCoins(self):
        return self.coins
    def getFruits(self):
        return self.fruits
    def getScares(self):
        return self.scares
    def getGhosts(self):
        return self.ghosts
    def draw(self, screen, pacmanState):
        self.drawWalls(screen)
        self.drawPassages(screen)
        self.drawCoins(screen)
        self.drawFruits(screen)
        self.drawDoors(screen)
        self.drawTeleports(screen)
        self.drawScares(screen)
        self.drawGhosts(screen, pacmanState)
        return
    def moveGhosts(self, pacmanPosition, PacmanState):
        for ghost in self.ghosts:
            if ghost.type == Enums.MapElement.GhostRed:
                # czerwony duch poruszas się w kierunku gracza zawsze niezależnie od tego gdzie jest gracz
                if PacmanState == Enums.PacmanState.Normal:
                    ghost.moveInDirection(ghost.getDirectionTowardsPacman(pacmanPosition), self.getWalls(), self.getTeleports())
            
            elif ghost.type == Enums.MapElement.GhostBlue:
                # niebieski duch porusza się w kierunku gracza, kiedy ten jest odpowienio blisko, w przeciwnym razie wykonuje losowe ruchy
                if PacmanState == Enums.PacmanState.Normal:
                    if ghost.isPacmanNear(pacmanPosition) == True:
                        ghost.moveInDirection(ghost.getDirectionTowardsPacman(pacmanPosition), self.getWalls(), self.getTeleports())
                    else:
                        ghost.makeRandomMove(None, self.getWalls(), self.getTeleports())
            
            elif ghost.type == Enums.MapElement.GhostPink:
                # różowy duch idzie w kierunku gracza jeżeli ten nie jest w jego pobliżu
                if PacmanState == Enums.PacmanState.Normal:
                    if ghost.isPacmanNear(pacmanPosition) == True:
                        ghost.makeRandomMove(None, self.getWalls(), self.getTeleports())
                    else:
                        ghost.moveInDirection(ghost.getDirectionTowardsPacman(pacmanPosition), self.getWalls(), self.getTeleports())
            
            elif ghost.type == Enums.MapElement.GhostOrange:
                #pomarańczowy duch goni gracza jeżeli nie znajduje się w jego pobliżu, jeżeli gracz jest blisko pomarańczowy ucieka
                if PacmanState == Enums.PacmanState.Normal:
                    if ghost.isPacmanNear(pacmanPosition) == True:
                        ghost.moveInDirection(ghost.getDirectionOppositePacman(pacmanPosition), self.getWalls(), self.getTeleports())
                    else:
                        ghost.moveInDirection(ghost.getDirectionTowardsPacman(pacmanPosition), self.getWalls(), self.getTeleports())

            if PacmanState == Enums.PacmanState.OnSteroids:
                ghost.moveInDirection(ghost.getDirectionOppositePacman(pacmanPosition), self.getWalls(), self.getTeleports())
            #ghost.makeMove()
    def checkVictoryCondition(self):
        if len(self.coins) <= 0:
            return True
        return False
    def drawVicoryScreen(self, screen):
        text = self.font.render("Victory!", False, (231, 254, 0))
        return screen.blit(text, (220,360))
    def spawnFruit(self, points, level):
        if points/level > 70 and self.fruitSpawned == False:
            index = (int)(len(self.passages) / 2)
            width = self.passages[index].width
            height = self.passages[index].height
            x = self.passages[index].x
            y = self.passages[index].y
            self.fruits.append(pygame.Rect((x, y), (width, height)))
            self.fruitSpawned = True
    def reset(self):
        self.fruitSpawned = False
        self.walls = []
        self.coins = []
        self.fruirs = []
        self.passages = []
        self.doors = []
        self.teleports = []
        self.scares = []
        self.ghosts = []
        self.getMap()
        return
