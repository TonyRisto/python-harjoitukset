class Elevator:
    def __init__(self, id, botFloor, topFloor):
        self.id = id
        self.botFloor = botFloor
        self.topFloor = topFloor
        self.currentFloor = botFloor

    def toFloor(self, floor):
        floor = min(max(floor, self.botFloor), self.topFloor)
        while self.currentFloor != floor:
            if self.currentFloor == floor:
                break
            if self.currentFloor < floor:
                self.moveUp()
            elif self.currentFloor > floor:
                self.moveDown()

        
    def moveUp(self):
        self.currentFloor += 1
        print(f"Hissi {self.id}: kerros {self.currentFloor}")

    def moveDown(self):
        self.currentFloor -= 1
        print(f"Hissi {self.id}: kerros {self.currentFloor}")

class House:
    def __init__(self, botFloor, topFloor, elevatorsCount):
        self.botFloor = botFloor
        self.topFloor = topFloor
        self.elevatorsCount = elevatorsCount
        self.elevators = []
        for i in range(elevatorsCount):
            self.elevators.append(Elevator(i, botFloor, topFloor))

    def runElevators(self, elevatorNumber, targetFloor):
        elevator = self.elevators[elevatorNumber]
        elevator.toFloor(targetFloor)

    def fireAlarm(self):
        for i in range(len(self.elevators)):
            self.runElevators(i, self.botFloor)

house = House(1, 15, 5)
house.runElevators(1, 6)
house.runElevators(2, 5)
house.fireAlarm()
for i in house.elevators:
    print(f"Hissi: {i.id} Kerros: {i.currentFloor}")