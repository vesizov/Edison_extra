import random


class Psychic:
    def __init__(self):
        self.number = None
        self.bingo = 0

    @staticmethod
    def third_eye(user_number):
        return user_number if bool(random.getrandbits(1)) else random.randint(10, 99)

    def abracadabra(self, user_number):
        self.number = self.third_eye(user_number)
        return self.number

# just for a joke purposes

kashpirovskiy = Psychic()
houdini = Psychic()
david_blaine = Psychic()
