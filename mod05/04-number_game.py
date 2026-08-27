import random

## Initialize the number

number = random.randint(1, 10)

## User's first guess

user_guess = int(input("Arvaa numero 1 ja 10 väliltä: "))

count = 0
while user_guess != number:
    if number > user_guess:
        print("Numero on isompi.")
    elif number < user_guess:
        print("Numero on pienempi.")
    user_guess = int(input("Arvaa uudestaan: "))
    count += 1

print(f"Oikein, numero oli {number}\nArvauskertoja: {count}")