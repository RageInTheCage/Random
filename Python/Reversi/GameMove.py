class GameMove(object):
    def __init__(self, playerNumber, x, y, flipCount):
        self.playerNumber = playerNumber
        self.x = x
        self.y = y
        self.flipCount = flipCount
        self.overturned = []

    def addOverturned(self, overturned):
        self.overturned.extend(overturned)
