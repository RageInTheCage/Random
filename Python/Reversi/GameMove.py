class GameMove(object):
    def __init__(self, playerNumber, x, y, overturned):
        self.playerNumber = playerNumber
        self.x = x
        self.y = y
        self.overturned = overturned
        self.flipCount = len(overturned)