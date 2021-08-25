from time import sleep
from Beeper import Beeper


class MorseSound:
    def __init__(self, speed):
        self.speed = speed
        self._beep_durations = {'.': 100, '-': 400}
        self._beeper = Beeper()

    def echo(self, morse_code):
        for char in morse_code:
            print(char, end='')
            if char in self._beep_durations:
                duration = self._beep_durations[char]
                self._beeper.beep(duration * self.speed)
                sleep(.05 * self.speed)
            else:
                sleep(.1 * self.speed)

        print()
