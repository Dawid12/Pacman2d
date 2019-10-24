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
    Fruit = 4
    Teleport = '6'
    Door = '7'
class MouthState(Enum):
    Open = 1
    Close = 2
class Moves(Enum):
    Right = (3, 0)
