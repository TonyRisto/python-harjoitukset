import random

points = int(input("Monta pistettä haluat arpoa? "))
save_points = 0.0
n = 0.0

while points > 0:
    x = random.random() * 2 - 1
    y = random.random() * 2 - 1
    if x**2 + y**2 < 1:
        n += 1
    points -= 1
    save_points += 1

pi_approximation = 4 * n / save_points
print(pi_approximation)