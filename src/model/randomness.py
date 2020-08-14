import math
from random import random


# //EFFECTS: Rolls a dice with a given random max value
def random_dice(x):
    return math.ceil(random() * x)
