from setup_functions import getName, getAge, evaluateAge, mainMenu, loadGame, newGame

with open("instructions.txt", "r") as file:
    instructions = file.read()

with open("welcome.txt", "r") as file:
    welcome = file.read()

name = getName()
isOldEnough, age = evaluateAge(getAge())

if not isOldEnough:
    print(f"Et ole tarpeeksi vanha, kokeile {12 - age} vuoden päästä uudestaan.")
else:
    print(f"\nTervetuloa pelaamaan kylänrakennuspeliä, {name}!\nValitse jokin seuraavista:\n")
    while True:
        command = mainMenu()

        if command == 1:
            input(f"\n{welcome}\n(paina enter jatkaaksesi)")
            newGame(name)

        if command == 2:
            input(f"{instructions}\npaina enter jatkaaksesi")

        if command == 3:
            loadGame()

        if command == 4:
            break