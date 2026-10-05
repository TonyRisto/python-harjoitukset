import json
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
            userInput = int(input("1. Uusi peli\n2. Ohjeet\n3. Jatka viimeisintä peliä\n4. Lopeta\n"))
            if userInput < 1 or userInput > 4:
                print("\nValinnan pitää olla 1-4 väliltä\n")
                continue
            else:
                return userInput
        except ValueError:
            print("\nValinnan pitää olla luku 1-4 väliltä\n")

def saveGame(game):
    saveData = {
        "player": game.player,
        "buildings": game.buildings,
        "resources": vars(game.resources),
        "sustainability": vars(game.sustainability)
    }
    with open("save.json", "w") as file:
        json.dump(saveData, file, indent=2)

def loadGame():
    try:
        with open("save.json", "r") as file:
            saveData = json.load(file)
    except FileNotFoundError:
        input("Ei tallennettua peliä. (jatka painamalla enter)")
        return mainMenu()

    game = GameState(saveData["player"])
    game.year = saveData.get("year", 1)
    game.buildings = saveData["buildings"]
    for key, value in saveData["resources"].items():
        setattr(game.resources, key, value)
    for key, value in saveData["sustainability"].items():
        setattr(game.sustainability, key, value)
    runGame(game)
    
def newGame(name):
    game = GameState(name)
    runGame(game)

def runGame(game):
    running = True
    while running:
        command = input(f"Valitse seuraavista toiminnoista:\n{commands}\n")
        if command == "rakenna":
            userInput = input(f"Valitse seuraavista rakennuksista:\n{game.getBuildingsList()}")
            input(f"{game.build(userInput)}\n paina enter jatkaaksesi")
        elif command == "tilanne":
            input(f"Tilanne\n{game.getStatus()}\n paina enter jatkaaksesi")
        elif command == "seuraava":
            game.advanceYear()
        elif command == "tallenna":
            saveGame(game)
            input("Peli tallennettu. (paina enter)")
        elif command == "lopeta":
            running = False
        else:
            print("Väärä komento.")