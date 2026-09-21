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

class ElectricCar(Car):
    def __init__(self, license, topSpeed, batteryCapacity):
        self.batteryCapacity = batteryCapacity
        super().__init__(license, topSpeed)

class CombustionCar(Car):
    def __init__(self, license, topSpeed, fuelTankCapacity):
        self.fuelTankCapacity = fuelTankCapacity
        super().__init__(license, topSpeed)

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

electric = ElectricCar("ABC-15", 180, "52.5 kWh")
petrol = CombustionCar("ACD-123", 165, "32.3 l")

electric.currentSpeed = 150
petrol.currentSpeed = 120

electric.travel(3)
petrol.travel(3)

print(electric.odometer)
print(petrol.odometer)