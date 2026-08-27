import random

dices_count = int(input("Anna noppien lukumäärä: "))

dices = []
dices_sum = 0

for i in range(dices_count):
    dices_count = random.randint(1, 6)
    dices.append(dices_count)
    dices_sum += dices_count


print(f"Noppien silmäluvut: {dices}")
print(f"Noppien silmälukujen summa: {dices_sum}")
#print(f"Noppien silmälukujen summa: {sum(dices)}")