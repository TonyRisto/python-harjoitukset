import random

participants = []

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

for i in range(1, 11):
    topSpeed = random.randint(100, 200)
    car = Car(f"ABC-{i}", topSpeed)
    participants.append(car)

while car.odometer < 10000:
    speeds = random.randint(-10, 15)
    for car in participants:
        car.accelerate(speeds)
        car.travel(1)
    if any(car.odometer >= 10000 for car in participants):
        break
        
for i in participants:
    print(f"Auto: {i.license}, Matkamittari: {i.odometer}, Huippunopeus: {i.topSpeed}, Nopeus lopussa: {i.currentSpeed}")
