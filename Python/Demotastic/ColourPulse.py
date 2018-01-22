import random


def get_random_step():
    return random.randint(-10, 10)


class ColourPulse:
    def __init__(self, min_value=0, max_value=255):
        self.colour_element = []
        self.colour_step = []
        self.min_value = min_value
        self.max_value = max_value
        self.reset()

    def reset(self):
        self.colour_element.clear()
        for index in range(0, 4):
            self.colour_element.append(self.get_random_colour_element())
            self.colour_step.append(get_random_step())

    def animate(self):
        for index in range(0, 4):
            self.colour_element[index] += self.colour_step[index]

            if self.min_value <= self.colour_element[index] <= self.max_value:
                continue

            self.colour_step[index] = -self.colour_step[index]
            self.colour_element[index] += self.colour_step[index] * 2

    def get_random_colour_element(self):
        return random.randint(self.min_value, self.max_value)

    @property
    def colour(self):
        return tuple(self.colour_element)
