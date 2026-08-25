cabin_class = input("Mikä on hyttiluokkasi? ")
cabin_class = cabin_class.upper()

if cabin_class == "LUX":
    print("Hyttisi on parvekkeellinen hytti yläkannella")
elif cabin_class == "A":
    print("Hyttisi on ikkunallinen autokannen yläpuolella")
elif cabin_class == "B":
    print("Hyttisi on ikkunaton autokannen yläpuolella")
elif cabin_class == "C":
    print("Hyttisi on ikkunaton autokannen alapuolella")
else: print("Virheellinen hyttiluokka")