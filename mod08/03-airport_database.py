airports = {}

def start():
    return int(input("\nHaluatko:\n1. Lisätä lentoaseman\n2. Etsiä lentoasemia\n3. Lopettaa\n"))

def add_airport():
    airportIcaoCode = input("Anna ICAO-koodi: ")
    airportName = input("Anna lentoaseman nimi: ")
    airports[airportIcaoCode] = airportName
    print(f"{airportName} lisätty.")

def find_airport():
    airportIcaoCode = input("Anna haettavan lentokentän ICAO-koodi: ")
    try:
        airport = airports[airportIcaoCode]
        print("\n" + airport)
    except KeyError:
        print("Lentokenttää ei löydy.")

def main():
    command = None
    while command != 3:
        command = start()

        if command == 1:
            add_airport()
        elif command == 2:
            find_airport()
        elif command == 3:
            print("Kiitos ja näkemiin!")
        else:
            print("Virheellinen syöte, yritä uudestaan.")

main()