import random

sides = int(input("Anna nopan tahkojen yhteismäärä: "))

def throw_dice(sides):
    dice_sides = sides
    dice = random.randint(1, dice_sides)
    return dice

dice = throw_dice(sides)
print(dice)

while dice != sides:
    dice = throw_dice(sides)
    print(dice)