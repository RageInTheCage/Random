import random


def get_random_step():
    return random.randint(-10, 10)


def get_random_colour_element():
    return random.randint(0, 255)


def bounds_have_been_exceeded(colour_value):
    return colour_value < 0 or colour_value > 255


class ColourPulse:
    def __init__(self):
        self.colour_element = []
        self.colour_step = []

        for index in range(0, 4):
            self.colour_element.append(get_random_colour_element())
            self.colour_step.append(get_random_step())

    def animate(self):
        for index in range(0, 4):
            self.colour_element[index] += self.colour_step[index]

            if 0 <= self.colour_element[index] <= 255:
                continue

            self.colour_step[index] = -self.colour_step[index]
            self.colour_element[index] += self.colour_step[index] * 2

    @property
    def colour(self):
        return tuple(self.colour_element)
