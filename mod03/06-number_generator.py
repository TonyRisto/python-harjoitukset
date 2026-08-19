import random

n1 = str(random.randint(0, 9))
n2 = str(random.randint(0, 9))
n3 = str(random.randint(0, 9))

three_number_code = n1 + n2 + n3

n4 = str(random.randint(1, 6))
n5 = str(random.randint(1, 6))
n6 = str(random.randint(1, 6))
n7 = str(random.randint(1, 6))

four_number_code = n4 + n5 + n6 + n7

print(f"Kolmen numeron koodi: {three_number_code}")
print(f"Neljän numeron koodi: {four_number_code}")