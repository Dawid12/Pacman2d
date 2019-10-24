import pygame
from Pacman import Pacman
from Map import Map
pygame.init()
pygame.font.init()
(screenWidth, screenHeight) = ((560, 720))
pacman = Pacman()
map = Map("data\\map.txt")
map.getMap()
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Pacman')
clock = pygame.time.Clock()
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        pacman.move(0, -1, map.getWalls(), map.getTeleports())
    elif pressed[pygame.K_DOWN]:
        pacman.move(0, 1, map.getWalls(), map.getTeleports())
    elif pressed[pygame.K_LEFT]:
        pacman.move(-1, 0, map.getWalls(), map.getTeleports())
    elif pressed[pygame.K_RIGHT]:
        pacman.move(1, 0, map.getWalls(), map.getTeleports())
    pacman.keepMoving(map.getWalls(), map.getTeleports())
    screen.fill((0,0,0))
    map.drawWalls(screen)
    map.drawPassages(screen)
    map.drawCoins(screen)
    map.drawDoors(screen)
    map.drawTeleports(screen)
    screen.blit(pacman.getSurface(), pacman.getPosition())
    screen.blit(pacman.getPointsSurface(), (0,0))
    screen.blit(pacman.getLifesSurface(), (200,0))
    screen.blit(pacman.getCoordSurface(), (0, 670))
    pygame.display.flip()
    clock.tick(120)

