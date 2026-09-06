name = input("Kirjoita nimi: ")

names = set()

while name != "":
    names.add(name)
    name = input("Uusi nimi: ")
    name = name.lower()
    name = name.capitalize()

    for i in names:
        if i == name:
            print("Aiemmin syötetty nimi")


for n in names:
    print(n)