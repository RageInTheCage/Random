class GameMove(object):
    def __init__(self, player_number, x, y, overturned):
        self.player_number = player_number
        self.x = x
        self.y = y
        self.overturned = overturned
        self.flipCount = len(overturned)
