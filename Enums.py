from enum import Enum
class Direction(Enum):
    Up = 1
    Down = 2
    Left = 3
    Right = 4
class MapElement(Enum):
    Wall = '0'
    Coin = '1'
    Passage = '2'
    Scare = '3'
    Fruit = 4
    Teleport = '6'
    Door = '7'
    GhostRed = 'A'
    GhostOrange = 'B'
    GhostBlue = 'C'
    GhostPink = 'D'
    Frightened = 'E'
    Eaten = 'F'
class PacmanState(Enum):
    Normal = 1
    OnSteroids = 2
class GhostState(Enum):
    Normal = 1
    Frightened = 2
    Eaten = 3
class MouthState(Enum):
    Open = 1
    Close = 2
class Moves(Enum):
    Right = (3, 0)
