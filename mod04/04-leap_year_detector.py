year = int(input("Anna vuosiluku (esim. 2020) "))

if year % 4:
    print(f"{year} ei ole karkausvuosi")
else:
    print(f"{year} on karkausvuosi")