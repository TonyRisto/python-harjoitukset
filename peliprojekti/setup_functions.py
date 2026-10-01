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
            userInput = int(input("1. Uusi peli\n2. Jatka peliä\n3. Ohjeet\n4. Lopeta\n"))
            if userInput < 1 or userInput > 4:
                print("\nValinnan pitää olla 1-4 väliltä\n")
                continue
            else:
                return userInput
        except ValueError:
            print("\nValinnan pitää olla luku 1-4 väliltä\n")