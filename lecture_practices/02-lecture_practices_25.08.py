age = int(input("Kerro ikäsi "))
species = input("Mikä laji olet? ")
species = species.lower()

print("Juomalista\nKahvi")

if age >= 18 and species == "ihminen":
    print("Viini")
if age >= 100 and species == "tonttu":
    print("Olut")
if species == "robotti":
    print("Öljy")