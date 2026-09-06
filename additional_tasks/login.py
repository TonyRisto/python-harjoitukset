accounts = [
{
    "username": "Tony",
    "password": "SaLaSaNa",
    "loginTries": 0
},
{
    "username": "Scala",
    "password": "Ohjelmointikieli",
    "loginTries": 0

}
]

key1 = "username"
key2 = "password"
key3 = "loginTries"


## Login tests if username and password match, if not, it will give a value of what was wrong.
def login(username, password):
    for i in accounts:
        if i[key1] == username and i[key2] == password and i[key3] < 3:
            loggedIn = True
            username = username
            loginTries = i[key3]
            return loggedIn, username, loginTries
        elif i[key1] == username and i[key2] != password:
            loggedIn = False
            username = username
            loginTries = i[key3]
            return loggedIn, username, loginTries
    return "Väärät tunnukset"


loggedIn = False
wrongPassword = 0


username = input("Anna käyttäjätunnus: ")
password = input("Anna salasana: ")

while loggedIn != True and wrongPassword < 3 and username != "":
    loggedIn = login(username, password)
    (loggedIn, username, loginTries) = loggedIn
    if loggedIn == True:
        print(f"Kirjauduttu sisään. Tervetuloa {username}.")
        quit()
    elif loggedIn == False:
        for i in accounts:
            if i[key1] == username and i[key3] < 3:
                i.update({"loginTries": loginTries + 1})
                print(f"Väärä salasana, kokeile uudestaan. Yrityksiä jäljellä: {3 - loginTries}")
            elif i[key1] == username and i[key3] == 3:
                print("Käyttäjätili lukittu. Kokeile eriä tiliä.")
    elif loggedIn == "Väärät tunnukset":
        print("Väärät tunnukset.")
    username = input("Anna käyttäjätunnus: ")
    password = input("Anna salasana: ")