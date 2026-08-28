import math

def pizza_price(diameter_cm, price_in_euros):
    radius_cm = diameter_cm / 2
    pizza_area_cm = math.pi * (radius_cm ** 2)
    pizza_area_m = pizza_area_cm / 10000
    pizza_price = price_in_euros / pizza_area_m
    return pizza_price

pizza1 = float(input("Kirjoita ensimmäisen pizzan halkaisija: "))
price1 = float(input("Kirjoita ensimmäisen pizzan hinta: "))

pizza2 = float(input("Kirjoita toisen pizzan halkaisija: "))
price2 = float(input("Kirjoita toisen pizzan hinta: "))

print(f"1. Pizzan hinta: {pizza_price(pizza1, price1):.2f}€ per neliömetri")
print(f"2. Pizzan hinta: {pizza_price(pizza2, price2):.2f}€ per neliömetri")

if pizza_price(pizza1, price1) == pizza_price(pizza2, price2):
    print("Pizzoissa on sama yksikköhinta.")
elif pizza_price(pizza1, price1) < pizza_price(pizza2, price2):
    print("Ensimmäisessä pizzassa on edullisempi yksikköhinta.")
else:
    print("Toisessa pizzassa on edullisempi yksikköhinta.")