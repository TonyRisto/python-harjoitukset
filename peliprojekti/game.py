name = input("Mikä on nimesi? ")
age = int(input("Mikä on ikäsi? "))

if age < 12:
    print(f"Kokeile {12 - age} vuoden päästä uudestaan :)")
    quit()

print(f"Hei, {age}-vuotias {name}!\nTervetuloa pelaamaan!")


while True:
    command = int(input("Valitse seuraavista komennoista:\n1. Aloita peli\n2. Ohjeet\n3. Tulostaulu\n4. Lopeta\n"))
    state = command
    while state != 4:
        if state == 1:
            state = input("Paina x näppäintä\n")
        if state == 2:
            state = input("Paina y näppäintä\n")
        if state == 3:
            state = input("Paina a näppäintä\n")
        if state == "x" or state == "y" or state == "a":
            command = int(input("Päävalikko: 1. Aloita peli, 2. Ohjeet, 3. Tulostaulu, 4. Lopeta\n"))
            state = command
        else:
            print("Väärä näppäin, aloita alusta.")
            break
        