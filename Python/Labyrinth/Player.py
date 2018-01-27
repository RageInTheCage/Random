import pygame


class Player:
    def __init__(self, maze, location):
        self.maze = maze
        self.location = location
        self.vectors = self.__get_vectors()
        self.colour = pygame.Color("yellow")

    def update(self):
        for vector in self.vectors:
            line = self.offset_vector(vector)
            self.maze.draw_line(line, self.colour, 3)

    def offset_vector(self, vector):
        return self.offset_point(vector[0]), self.offset_point(vector[1])

    def offset_point(self, point):
        return point[0] + self.location[0], point[1] + self.location[1]

    @staticmethod
    def __get_vectors():
        return (
            ((0, 0), (1, 1)),
            ((0, 1), (1, 0))
        )
