n1 = input("Anna alkava luku: ")
n2 = input("Anna päättyvä luku: ")

number = 0

while n1 == str(n1) and n2 == str(n2):
    try:
        n1 = int(n1)
        n2 = int(n2)
    except ValueError:
        print("Väärä syöte, kokeile uudestaan.")
        n1 = input("Anna alkava luku: ")
        n2 = input("Anna päättyvä luku: ")

while number <= n2:
    if number % 3 == 0:
        print(number)
    number += 1