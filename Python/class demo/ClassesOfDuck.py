from colorama import Fore


class Duck:
    direction = None
    colour = None
    gender = None
    legs = 2

    def __init__(self, who_migrates):
        self.direction = who_migrates
        self.colour = Fore.GREEN
        self.gender = "Female"

    def say(self, what):
        print(self.colour + what + Fore.RESET)

    def fly(self):
        self.say('"I am flying {}"'.format(self.direction))

    def call(self):
        self.say('"Quack, quack"')

    def describe(self):
        self.say("Class = {}, Gender = {}, Legs = {}"
                 .format(
                    type(self).__name__, self.gender, self.legs
                    )
                )


class Mallard(Duck):
    def __init__(self, who_migrates):
        self.colour = Fore.BLUE
        self.direction = who_migrates
        self.gender = "Male"

    def call(self):
        self.say('(louder) "Quack!"')


class Decoy(Duck):
    def __init__(self):
        self.colour = Fore.YELLOW
        self.legs = 0

    def fly(self):
        self.say('"Fly?!  Not likely!"')

    def call(self):
        self.say('"Honk"')
