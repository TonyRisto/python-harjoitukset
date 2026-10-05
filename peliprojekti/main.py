from setup_functions import getName, getAge, evaluateAge, mainMenu, loadGame, newGame

with open("instructions.txt", "r") as instruction:
    instructions = instruction.read()

name = getName()
isOldEnough, age = evaluateAge(getAge())

if not isOldEnough:
    print(f"Et ole tarpeeksi vanha, kokeile {12 - age} vuoden päästä uudestaan.")
else:
    while True:
        command = mainMenu()

        if command == 1:
            newGame(name)

        if command == 2:
            input(f"{instructions}\npaina enter jatkaaksesi")
            mainMenu()

        if command == 3:
            loadGame()

        if command == 4:
            break