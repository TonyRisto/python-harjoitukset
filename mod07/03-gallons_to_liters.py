def gallons_to_liters(gallon):
    liter = gallon * 3.785
    return liter

gallons = float(input("Kirjoita määrä gallonoina: "))
print(gallons_to_liters(gallons))

while gallons > -1:
    gallons = float(input("Kirjoita määrä gallonoina: "))
    if gallons > 0:
        print(gallons_to_liters(gallons))