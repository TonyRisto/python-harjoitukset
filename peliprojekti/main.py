from setup_functions import getName, getAge, evaluateAge, mainMenu, runGame
from classes import GameState
from texts import instructions

name = getName()
isOldEnough, age = evaluateAge(getAge())

if not isOldEnough:
    print(f"Et ole tarpeeksi vanha, kokeile {12 - age} vuoden päästä uudestaan.")
else:
    command = mainMenu()

if command == 1:
    runGame()

if command == 2:
    input(f"{instructions}\npaina enter jatkaaksesi")
    mainMenu()

if command == 3:
    quit()