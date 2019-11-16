import pygame
import Enums
from Pacman import Pacman
from Map import Map
from Move import Move
import time
pygame.init()
pygame.font.init()
frames = 30
(screenWidth, screenHeight) = ((560, 720))
pacman = Pacman()
map = Map("data\\map.txt")
map.getMap()
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Pacman')
clock = pygame.time.Clock()
running = True
pacmanMove = Move.initWithDirection(Enums.Direction.Left)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        pacmanMove = Move.initWithDirection(Enums.Direction.Up)
    elif pressed[pygame.K_DOWN]:
        pacmanMove = Move.initWithDirection(Enums.Direction.Down)
    elif pressed[pygame.K_LEFT]:
        pacmanMove = Move.initWithDirection(Enums.Direction.Left)
    elif pressed[pygame.K_RIGHT]:
        pacmanMove = Move.initWithDirection(Enums.Direction.Right)

    pacman.move(pacmanMove, map.getWalls(), map.getTeleports(), map.getCoins(), map.getScares(), map.getGhosts())
    map.moveGhosts(pacman.getPosition(), pacman.getPacmanState())
    screen.fill((0,0,0))
    map.draw(screen, pacman.getPacmanState())
    pacman.draw(screen)

    if map.checkVictoryCondition():
        map.drawVicoryScreen(screen);
        pygame.display.flip()
        time.sleep(10)
        map.reset()
        pacman.reset()
        pacman.draw(screen)
        map.draw(screen, pacman.getPacmanState())
        continue
    if pacman.isDead():
        running = pacman.handleDeath(screen)
    pygame.display.flip()
    clock.tick(frames)


    #pacman todo
    # - jedzenie owocow
    # - ruchy duchow
