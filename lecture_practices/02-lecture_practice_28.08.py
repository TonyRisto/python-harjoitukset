weapon = input("Maria oli rohkea ritari, joka joutui kaksintaisteluun. Minkä aseen Maria ottaa? ")
weapon = weapon.lower()

items = ["Kranaatti", "Kilpi", "Konekivääri"]
while weapon != "miekka":
    print(f"{weapon.capitalize()} on huono ase, anna toinen ase.")
    weapon = input("Maria oli rohkea ritari, joka joutui kaksintaisteluun. Minkä aseen Maria ottaa? ")
    weapon = weapon.lower()


print(f"Marian ase on {weapon} jolla hän voittaa varmasti!")

other_items = input("Haluatko ottaa jotain muutakin mukaan kaksintaisteluun? (kyllä/ei)")

while True:
    if other_items == "ei":
        print(f"Onnea kaksintaisteluun {weapon}si kanssa.")
        state = 0
        break
    if other_items == "kyllä":
        state = 1
        break
    else:
        print("Väärä valinta, kokeile uudestaan.")
    input("Haluatko ottaa jotain muutakin mukaan kaksintaisteluun? (kyllä/ei)")

if state == 1:
    print(f"Tässä lista tavaroista, joita voit ottaa taisteluun mukaan:\n{items}")