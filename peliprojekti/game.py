name = input("Mikä on nimesi? ")
age = int(input("Mikä on ikäsi? "))
item_list = []

if age < 12:
    print(f"Kokeile {12 - age} vuoden päästä uudestaan :)")
    quit()

print(f"Hei, {age}-vuotias {name}!\nTervetuloa pelaamaan!")

def main_menu():
    return int(input("1. Pelaa\n2. Ohjeet\n3. Lopeta\n"))

def play():
    print("Pelataan!")

def add_items(item1, item2, item3):
    item_list.append(item1)
    item_list.append(item2)
    item_list.append(item3)

def show_list(item_list):
    for i in range(len(item_list)):
        while i > -1:
            print(f"Repussasi on: {item_list[i]}")
            i -= 1

def instructions():
    print("Opettele pelaan")

def main():
    command = None
    while command != 0:
        command = main_menu()

        if command == 1:
            play()
        elif command == 2:
            instructions()
        elif command == 3:
            print("Hei hei!")
            quit()
        else:
            print("Tuntematon valinta.")

main()