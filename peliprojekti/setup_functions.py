import json
from classes import GameState
from data import commands
import os


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

# Päävalikko tarvitsee käyttäjältä syötteen numerona ja palauttaa sen. (tarkistaa myös onko syöte oikein)

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

# Tallentaa käyttäjän pelin tilanteen, ottaen game oliosta tarvittavat tiedot (tallentaa JSON tiedostona, yksi tallennus voi olla kerrallaan).

def saveGame(game):
    saveData = {
        "year": game.year,
        "player": game.player,
        "buildings": game.buildings,
        "resources": vars(game.resources),
        "sustainability": vars(game.sustainability)
    }
    with open("save.json", "w") as file:
        json.dump(saveData, file, indent=2)

# Lataa tallennuksen, luo GameState olion ja asettaa tallennuksessa olevat tiedot GameStateen (eli ns. jatketaan mihin on jääty).

def loadGame():
    try:
        with open("save.json", "r") as file:
            saveData = json.load(file)
    except FileNotFoundError:
        input("Ei tallennettua peliä. (jatka painamalla enter)")
        return

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

# Pelin pyörittämisfunktio. Tämä pyörittää koko peliä.

def runGame(game):
    print(game.getStatus())
    input("\nPaina enter jatkaaksesi")
    running = True
    while running:
        command = input(f"\nValitse seuraavista toiminnoista:\n{commands}\n")
        if command == "rakennukset":
            print(f"\nRAKENNUKSESI\n{game.getBuildings()}")
            menu = True
            while menu:
                userInput = input(f"\nValitse seuraavista:\n\nrakenna\npalaa\n").lower()
                if userInput == "rakenna":
                    print(game.getBuildingsList())
                    building = True
                    while building:
                        buildingInput = input("Anna rakennuksen nimi, jonka haluat rakentaa (kirjoita palaa, kun haluat takaisin)\n").lower()
                        if buildingInput == "palaa":
                            building = False
                        else:
                            print(f"{game.build(buildingInput)}")
                elif userInput == "palaa":
                    menu = False
                else:
                    print("Väärä komento, kirjoita rakenna tai palaa.")
        elif command == "kulutus":
            input(f"{game.getSpending()}\n(paina enter jatkaaksesi)")
        elif command == "tilanne":
            input(f"Tilanne\n{game.getStatus()}\n(paina enter jatkaaksesi)")
        elif command == "seuraava":
            game.advanceYear()
            result = game.checkEndGame()
            if result:
                input(f"{result} (paina enter jatkaaksesi)")
                running = False
                try:
                    os.remove("save.json")
                except FileNotFoundError:
                    pass
            print(game.getStatus())
        elif command == "tallenna":
            saveGame(game)
            input("Peli tallennettu. (paina enter jatkaaksesi)")
        elif command == "paavalikko":
            running = False
        else:
            print("Väärä komento.")