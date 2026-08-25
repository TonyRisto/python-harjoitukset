year = int(input("Anna vuosiluku (esim. 2020) "))

if year % 400 == 0:
    print(f"{year} on karkausvuosi")
elif (year % 4 == 0) and (year % 100 != 0):
    print(f"{year} on karkausvuosi")
else:
    print(f"{year} ei ole karkausvuosi")