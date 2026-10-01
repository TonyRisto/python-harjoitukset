from classes import GameState
from texts import commands

def getName():
    return input("Mikä on nimesi?\n").capitalize()

def getAge():
    while True:
        try:
            return int(input("Kuinka vanha olet?\n"))
        except ValueError:
            print("Syötä kokonaisluku")
            continue

def evaluateAge(age):
    if age >= 12:
        return True, age
    else:
        return False, age

def mainMenu():
    while True:
        try:
            userInput = int(input("1. Uusi peli\n2. Ohjeet\n3. Lopeta\n"))
            if userInput < 1 or userInput > 3:
                print("\nValinnan pitää olla 1-3 väliltä\n")
                continue
            else:
                return userInput
        except ValueError:
            print("\nValinnan pitää olla luku 1-3 väliltä\n")

def runGame():
    game = GameState()
    quit = False
    while not quit:
        command = input(f"Valitse seuraavista toiminnoista:\n{commands}\n")
        if command == "rakenna":
            userInput = input(f"Valitse seuraavista rakennuksista:\n{game.getBuildingsList()}")
            input(f"{game.build(userInput)}\n paina enter jatkaaksesi")
        elif command == "tilanne":
            input(f"Tilanne\n{game.getStatus()}\n paina enter jatkaaksesi")
        elif command == "seuraava":
            game.advanceYear()
        elif command == "lopeta":
            quit = True
        else:
            print("Väärä komento.")