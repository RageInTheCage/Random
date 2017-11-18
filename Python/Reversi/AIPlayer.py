import random


class AIPlayer(object):
    def __init__(self, player_number, game_board):
        self.player_number = player_number
        self.board = game_board


    def make_move(self, graphics):
        player_character = self.board.get_player_character(self.player_number)
        print("Player {0} is thinking...".format(player_character))

        self.board.assess_board(self.player_number)

        best_move = random.choice(self.get_best_moves())

        self.board.try_to_make_move(self.player_number, best_move.x, best_move.y)
        graphics.draw_board()
        graphics.update()

    def get_move_score(self, move):
        moveScore = self.get_location_score(move.x, move.y)
        for location in move.overturned:
            locationX = location[0]
            locationY = location[1]
            moveScore += self.get_location_score(locationX, locationY)
        return moveScore

    def get_location_score(self, x, y):
        if self.is_corner(x, y):
            return 20
        if self.is_edge(x, y):
            return 10
        if self.is_inner_corner(x, y) and self.is_corner_unprotected(x, y):
            return -10
        return 1

    def is_corner(self, x, y):
        return self.is_coordinate_an_edge(x) and self.is_coordinate_an_edge(y)

    def is_edge(self, x, y):
        if self.is_corner(x, y):
            return False
        return self.is_coordinate_an_edge(x) or self.is_coordinate_an_edge(y)

    def is_coordinate_an_edge(self, coordinate):
        return coordinate == 0 or coordinate == 7

    def is_inner_corner(self, x, y):
        return (x == 1 or x == 6) and (y == 1 or y == 6)

    def is_corner_unprotected(self, innerCornerX, innerCornerY):
        cornerX = self.get_edge_nearest(innerCornerX)
        cornerY = self.get_edge_nearest(innerCornerY)
        return self.board.get_player_at(cornerX, cornerY) != self.player_number

    def get_edge_nearest(self, coordinate):
        if coordinate < 4:
            return 0
        return 7

    def get_best_moves(self):
        bestMoveScore = None
        bestMoves = []

        for key, move in self.board.moves.items():
            moveScore = self.get_move_score(move)
            if bestMoveScore is None or moveScore > bestMoveScore:
                bestMoveScore = moveScore
                bestMoves = [move]
            elif moveScore == bestMoveScore:
                bestMoves.append(move)

        return bestMoves


