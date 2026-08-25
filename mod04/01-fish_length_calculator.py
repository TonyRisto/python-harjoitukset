pikeperch_length = float(input("Anna kuhan pituus senttimetreinä: "))

if pikeperch_length < 37:
    print(f"Laske kuha takaisin kasvamaan, pituudesta puuttuu {37 - pikeperch_length:.1f} cm")
else:
    print("Kuha on sallitussa pyyntimitassa")