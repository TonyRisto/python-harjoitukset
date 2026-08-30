temperature = float(input("Kirjoita lämpötila "))
academic_credit = int(input("Kirjoita opintopisteiden määrä "))
is_warm = input("Onko lämmin vai kylmä? ")
is_cloudy = input("Onko pilvinen sää vai ei? ")

fish_length = float(input("Kirjoita kalan pituus: "))
fish_age = int(input("Kirjoita kalan ikä: "))

week_day = input("Mikä päivä? (ma/ti/ke/to/pe/la)")
age = int(input("Mikä on ikäsi?"))


if temperature < 0:
    print("Lämpötila on alle 0 astetta")
else:
    print("Lämpötila on yli 0 astetta")

if academic_credit >= 150:
    print("Vähintään 150op")
else:
    print("Opintopisteitä on alle 150")

if is_warm == "lämmin":
    print("Sää on lämmin")
else:
    print("Sää on kylmä")

if is_cloudy == "pilvinen":
    print("Pilvinen sää")
else:
    print("Ei ole pilvistä")

if 10 < fish_length <= 65 or fish_age > 10:
    print("Kalan pituus on 10-65 välillä ja/tai kalan ikä on yli 10 vuotta")
else:
    print("Kumpikaan ehto ei täyttynyt")