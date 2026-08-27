numbers = []
number = input("Anna luku: ")

while number != "":
    numbers.append(number)
    number = input("Anna luku: ")

float_numbers = []
for n in numbers:
    float_numbers.append(float(n))

float_numbers.sort(reverse=True)
five_biggest = float_numbers[:5]
print(f"Suuruusjärjestys: {five_biggest}")