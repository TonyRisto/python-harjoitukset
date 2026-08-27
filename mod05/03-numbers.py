smallest = 0
highest = 0

input_number = input("Anna numero: ")

if input_number != "":
    number = float(input_number)
    smallest, highest = number, number

while input_number != "":
    number = float(input_number)
    if number < smallest:
        smallest = number
    if number > highest:
        highest = number
    input_number = input("Anna numero: ")

print(f"Pienin: {smallest}\nSuurin: {highest}")