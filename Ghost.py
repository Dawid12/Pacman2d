from Character import Character
import Enums
class Ghost(Character):
    def __init__(self, imageDict, type, x, y):
        self.image = imageDict[type]
        self.imageDict = imageDict
        self.type = type
        self.x = x
        self.y = y
        self.state = Enums.GhostState.Normal
    def setRect(self, rect):
        self.rect = rect
    def getRect(self):
        return self.rect
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
    def makeMove(self):
        return
