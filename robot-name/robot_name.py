from random import choice
from string import ascii_uppercase, digits

AVAILABLE_NAMES = [''.join([a, b, c, d, e])
                   for a in ascii_uppercase
                   for b in ascii_uppercase
                   for c in digits
                   for d in digits
                   for e in digits
                   ]


class Robot:
    def __init__(self):
        self.name = choice(AVAILABLE_NAMES)
        AVAILABLE_NAMES.remove(self.name)

    def reset(self):
        self.__init__()
