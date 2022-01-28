import random


class Psychic:
    def __init__(self):
        self.number = None
        self.sense_level = 0
        self.magic_count = 0
        self.bingo = 0

    @staticmethod
    def third_eye(user_number):
        return user_number if bool(random.getrandbits(1)) else random.randint(10, 100)

    def abracadabra(self, user_number):
        self.magic_count += 1
        self.number = self.third_eye(user_number)

        if self.number == user_number:
            self.bingo += 1
        self.sense_level = self.bingo / self.magic_count

        return self.number


kashpirovskiy = Psychic()
houdini = Psychic()
david_blaine = Psychic()
