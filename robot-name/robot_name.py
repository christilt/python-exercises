from string import ascii_uppercase, digits
import random

class Robot:
    names = list()

    def __init__(self):
        self.reset()

    def reset(self):
        name = self.__make_name()
        while(name in self.names):
            name = self.__make_name()
        self.name = name
        self.names.append(name)

    def __make_name(self):
        name = ''
        name += random.choice(ascii_uppercase)
        name += random.choice(ascii_uppercase)
        name += random.choice(digits)
        name += random.choice(digits)
        name += random.choice(digits)
        return name



