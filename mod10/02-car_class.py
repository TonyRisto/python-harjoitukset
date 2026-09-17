import random

carList = []

class Car:
    def __init__(self, license, topSpeed, currentSpeed = 0, odometer = 0):
        self.license = license
        self.topSpeed = max(0, topSpeed)
        self.currentSpeed = currentSpeed
        self.odometer = odometer

    def accelerate(self, speedChange):
        self.currentSpeed = max(0, min(self.currentSpeed + speedChange, self.topSpeed))

    def travel(self, hours):
        self.odometer = self.odometer + (hours * self.currentSpeed)

class Race:
    def __init__(self, name, length, carList):
        self.name = name
        self.length = length
        self.carList = carList

    def timePasses(self):
        speeds = random.randint(-10, 15)
        for i in self.carList:
            i.accelerate(speeds)
            i.travel(1)

    def showResults(self):
        for i in self.carList:
            print(f"Auto: {i.license}, Matkamittari: {i.odometer}, Huippunopeus: {i.topSpeed}, Nopeus: {i.currentSpeed}")

    def raceOver(self):
        race = True
        for i in range(len(self.carList)):
            if self.carList[i].odometer >= self.length:
                race = False
        return race


for i in range(1, 11):
    topSpeed = random.randint(100, 200)
    car = Car(f"ABC-{i}", topSpeed)
    carList.append(car)

greatDerby = Race("Suuri romuralli", 8000, carList)
race = True
hours = 0
while race == True:
    greatDerby.timePasses()
    race = greatDerby.raceOver()
    hours += 1
    if hours % 10 == 0:
        print(f"{hours}. tunti")
        greatDerby.showResults()

print(f"Lopputulokset:")
greatDerby.showResults()