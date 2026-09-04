import random

sides = int(input("Anna nopan tahkojen yhteismäärä: "))

def throw_dice(sides):
    dice = random.randint(1, sides)
    return dice

dice = throw_dice(sides)

while dice != sides:
    dice = throw_dice(sides)
    print(dice)