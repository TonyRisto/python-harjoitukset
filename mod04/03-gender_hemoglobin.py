gender = input("Mikä on biologinen sukupuolesi? (M/N) ")
gender = gender.lower()

if (gender != "m") and (gender != "n"):
    print("Väärä sukupuolisyöte")
    quit()

hemoglobin = int(input("Mikä on hemoglobiiniarvosi? "))


if (gender == "m") and (195 >= hemoglobin >= 134):
    print("Hemoglobiiniarvosi on normaali")
elif gender == "m" and hemoglobin > 195:
    print("Hemoglobiiniarvosi on korkea")
elif gender == "m" and hemoglobin < 134:
    print("Hemoglobiiniarvosi on alhainen")

if (gender == "n") and (175 >= hemoglobin >= 117):
    print("Hemoglobiiniarvosi on normaali")
elif gender == "n" and hemoglobin > 175:
    print("Hemoglobiiniarvosi on korkea")
elif gender == "n" and hemoglobin < 117:
    print("Hemoglobiiniarvosi on alhainen")