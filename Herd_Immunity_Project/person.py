import random

class Person(object):\

    def __init__(self, _id, is_vaccinated, infected=None):
        self._id = _id
        self.is_vaccinated = is_vaccinated
        self.infected = infected
        self.is_alive = True


    def did_survive_infection(self):
        rand = random.random()

        if self.infected is None:
            return True

        if rand < self.infected.kill_rate:
            self.is_alive = False
            return False
        else:
            self.infected = None
            self.is_vaccinated = True
            return True
