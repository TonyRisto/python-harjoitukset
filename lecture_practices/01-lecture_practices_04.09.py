import random

floatNumbers = []
floatNumbers2 = [25.0, 20.5, 19.25, 5.218, 215.21]
floatNumbersList = [floatNumbers, floatNumbers2]
floatNumbersAverage = []

def createFloats(floatNumbers):
    times = random.randint(5, 7)
    for i in range(0, times):
        while times > i:
            times -= 1
            numbers = random.randint(0, 100)
            randomFloat = random.random()
            floatNumber = numbers + randomFloat
            floatNumbers.append(floatNumber)

createFloats(floatNumbers)

def average(floatNumbers):
    numbers = 0
    for i in floatNumbers:
        numbers += i
    return numbers / len(floatNumbers)

result = average(floatNumbers)
print(result)

def averageGrade(floatNumbersList):
    averagesList = []
    for i in floatNumbersList:
        averages = average(i)
        averagesList.append(averages)
    return averagesList


results = averageGrade(floatNumbersList)
print(f"Keskiarvo: {results: .f2}")