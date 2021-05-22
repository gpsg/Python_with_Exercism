from random import choice, shuffle, seed
from string import ascii_uppercase, digits

AVAILABLE_NAMES = [''.join([a, b, c, d, e])
                   for a in ascii_uppercase
                   for b in ascii_uppercase
                   for c in digits
                   for d in digits
                   for e in digits
                   ]
shuffle(AVAILABLE_NAMES)

class Robot:
    def __init__(self):
        self.name = choice(AVAILABLE_NAMES)
        AVAILABLE_NAMES.remove(self.name)

    def reset(self):
        self.__init__()


if __name__ == '__main__':
    name_re = r'^[A-Z]{2}\d{3}$'
    # Set a seed
    a_seed = "Totally random."
    # Initialize RNG using the seed
    seed(a_seed)

    # Call the generator
    robot = Robot()
    name = robot.name

    # Reinitialize RNG using seed
    seed(a_seed)

    # Call the generator again
    robot.reset()
    name2 = robot.name

    print(name)
    print(name2)
    print(name2 == name_re)
