months = (
    "tammikuu",
    "helmikuu",
    "maaliskuu",
    "huhtikuu",
    "toukokuu",
    "kesäkuu",
    "heinäkuu",
    "elokuu",
    "syyskuu",
    "lokakuu",
    "marraskuu",
    "joulukuu"
)


month = int(input("Anna kuukauden numero: "))
season = months[month - 1]

if month <= 2 or month == 12:
    print("Talvi")
elif month <= 3 or month <= 5:
    print("Kevät")
elif month <= 6 or month <= 8:
    print("Kesä")
else:
    print("Syksy")