import random

length = int(input("Anna halutun numerokoodin pituus: "))
n1 = int(input("Anna numerovälin ensimmäinen numero: "))
n2 = int(input("Anna numerovälin viimeinen numero: "))
number_code = []

for i in range(length):
    randomizer = str(random.randint(n1, n2))
    print(randomizer, end="")
print()