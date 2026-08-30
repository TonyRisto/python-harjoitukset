kilograms = float(input("Kirjoita paino kilogrammoina: "))

grams = kilograms * 1000

lots = grams / 13.3
pounds = lots / 32
talents = pounds / 20

if lots < 1:
    print("Paino ei vastaa yhtään kokonaista luotia.")
else:
    print(f"Luodit: {lots:.0f}")
if pounds < 1:
    print("Paino ei vastaa yhtään kokonaista naulaa.")
else:
    print(f"Naulat: {pounds:.0f}")
if talents < 1:
    print("Paino ei vastaa yhtään kokonaista leiviskää.")
else:
    print(f"Leiviskät: {talents:.0f}")