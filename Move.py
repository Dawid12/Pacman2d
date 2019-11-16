import Enums
class Move:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    @classmethod
    def initWithDirection(cls, direction):
        if direction == Enums.Direction.Up:
            return cls(0, -5)
        elif direction == Enums.Direction.Down:
            return cls(0, 5)
        elif direction == Enums.Direction.Left:
            return cls(-5, 0)
        elif direction == Enums.Direction.Right:
            return cls(5, 0)