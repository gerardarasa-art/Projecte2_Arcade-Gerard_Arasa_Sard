import random


class robot:
    name = "machine"
    game = ["pedra","paper","tisora"]

    def playing(self):
        choice = random.choice(self.game)
        return choice
