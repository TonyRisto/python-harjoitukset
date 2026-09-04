import random

def throw_dice():
    dice = random.randint(1, 6)
    return dice

dice = throw_dice()

while dice != 6:
    dice = throw_dice()
    print(dice)