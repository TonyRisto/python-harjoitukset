year = int(input("Anna vuosi: "))

while year >= 1896:
    if year == 2021:
        print(f"Vuonna {year} oli olympialaiset poikkeuksellisesti koronan takia (2020 peruuntunut).")
    elif year == 1916:
        print(f"Vuonna {year} ei poikkeuksellisesti järjestetty olympialaisia ensimmäisen maailmansodan puhkeamisen vuoksi.")
    elif year == 1940:
        print(f"Vuoden {year} olympialaiset peruttiin toisen maailmansodan takia.")
    elif year == 1944:
        print(f"Vuonna {year} ei järjestetty olympialaisia toisen maailmansodan jatkumisen takia.")
    elif (year % 4) == 0:
        print(f"{year} oli olympiavuosi")
    else:
        print(f"{year} ei ollut olympialaisia")
    year = int(input("Anna vuosi: "))

print(f"Vuonna {year} ei ollut olympialaisia (aika ennen moderneja olympialaisia).")