username = "python"
password = "rules"

user = input("Anna käyttäjätunnus: ")
user_password = input("Anna salasana: ")

tries = 0

while (user != username or user_password != password) and tries < 4:
    if user != username:
        print("Väärä käyttäjätunnus")
    if user_password != password:
        print("Väärä salasana")
    print(f"{4 - tries} yritystä jäljellä")
    user = input("Anna käyttäjätunnus: ")
    user_password = input("Anna salasana: ")
    tries += 1

if username == user and password == user_password:
    print("Tervetuloa")
else:
    print("Pääsy evätty")