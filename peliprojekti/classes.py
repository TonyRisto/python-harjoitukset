from data import (
    BUILDINGS,
    DECAY,
    ENERGY_PER_CAPITA,
    FOOD_PER_CAPITA,
    INCOME_PER_CAPITA,
    GROWTH_RATE,
    DECLINE_RATE_UNHAPPINESS,
    DECLINE_RATE_HUNGER,
    HAPPINESS_GROWTH_MIN,
    HAPPINESS_DECLINE_MIN
)

# Resurssit luokka pitää kirjaa tämänhetkisestä väkiluvusta, rahan ja ruoan määrästä.
# Se sisältää myös metodit joilla saadaan energian ja ruoan kulutus sekä tulot.
# Ylläolevat riippuvat väkiluvun määrästä.

class Resources:
    def __init__(self):
        self.population = 100
        self.money = 500000
        self.food = 100

    def getEnergyConsumption(self):
        return self.population * ENERGY_PER_CAPITA

    def getFoodConsumption(self):
        return self.population * FOOD_PER_CAPITA

    def getIncome(self):
        return self.population * INCOME_PER_CAPITA


# Kestävyys luokka pitää kirjaa kestävyystavoitteista prosentteina.
# Lukuja muuttaa change metodi, joka varmistaa ettei luku mene alle 0:n tai yli 100:n

class Sustainability:
    def __init__(self):
        self.cleanWater = 50
        self.renewableShare = 0
        self.education = 50
        self.equality = 50
        self.environment = 50
        self.happiness = 50

    def change(self, name, amount):
        value = getattr(self, name) + amount
        setattr(self, name, max(0, min(100, value)))

# Pelin tila luokka huolehtii pelin pyörittämisestä ja rakennuksien määrästä sekä resurssi- ja kestävyysolioiden muutoksista.

class GameState:
    def __init__(self, player = None):
        self.player = player
        self.year = 1
        self.resources = Resources()
        self.sustainability = Sustainability()
        self.buildings = {
            "talo": 10,
            "maatila": 3,
            "vesitorni": 1,
            "koulu": 1,
            "hakevoimalaitos": 1
        }

# Pyörittää peliä yhden vuoden eteenpäin, päivittää resurssit ja kestävyysprosentit

    def advanceYear(self):
        self.resources.money += self.resources.getIncome() - self.getTotal("upkeep")
        self.resources.food += self.getTotal("foodProduction") - self.resources.getFoodConsumption()
        energyBalance = self.getTotal("energyProduction") - self.resources.getEnergyConsumption()
        self.sustainability.renewableShare = self.getRenewableShare()

        # Vuosittainen vähennys

        for key, value in DECAY.items():
            self.sustainability.change(key, value)

        if energyBalance < 0:
            self.sustainability.change("happiness", -5)
            self.sustainability.change("equality", -2)

        # Rakennusten vaikutus

        for name, count in self.buildings.items():
            for key, value in BUILDINGS[name].items():
                if key in ("cleanWater", "education", "equality", "environment", "happiness"):
                    self.sustainability.change(key, value * count)
        
        self.updatePopulation()
        self.year += 1

# Tekee tarkistuksen onko peli voitettu tai hävitty

    def checkEndGame(self):
        s = self.sustainability
        goals = [s.cleanWater, s.education, s.environment, s.equality, s.happiness, s.renewableShare]
        if self.resources.money <= 0:
            return "Kyläsi meni konkurssiin. Hävisit pelin"
        if self.resources.population <= 0:
            return "Kyläsi autioitui. Hävisit pelin"
        if self.resources.population >= 250 and all(g >= 70 for g in goals):
            return f"Onnittelut! Rakensit kestävän kylän vuodessa {self.year}."
        if s.renewableShare >= 75 and s.environment >= 75:
            return "Ekologinen voitto: kylästäsi tuli vihreän energian edelläkävijä!"
        if self.resources.money >= 1100000:
            return "Taloudellinen voitto: kylästäsi tuli rikas, mutta onko se kestävä?"
        if s.environment <= 0 and s.happiness <= 0:
            return "Kyläsi ympäristö tuhoutui ja asukkaista tuli onnettomia. Hävisit pelin"
        if self.year > 15 and s.environment <= 40:
            return "Aika loppui. Kyläsi ympäristö kärsi kasvun hinnasta."
        if self.year > 15 and s.education <= 40:
            return "Aika loppui. Kyläsi kärsi huonosta koulutuksesta."
        if self.year > 15 and s.equality <= 40:
            return "Aika loppui. Kyläsi kärsi tasa-arvon puutteesta."
        if self.year > 15 and s.cleanWater <= 40:
            return "Aika loppui. Kyläsi kärsi puhtaan veen saatavuudesta."
        if self.year > 15:
            return "Aika loppui, et saavoittanut tavoitteitasi."
        return None

# Hakee avaimen mukaan kokonaiskulutuksen, esim. ylläpidon kustannukset yhteensä.

    def getTotal(self, key):
        total = 0
        for name, count in self.buildings.items():
            total += BUILDINGS[name].get(key, 0) * count
        return total

# Hakee uusiutuvan energian tuotannon määrän suhteessa energian tuotantoon.

    def getRenewableShare(self):
        production = self.getTotal("energyProduction")
        if production == 0:
            return 0
        renewable = 0
        for name, count in self.buildings.items():
            if BUILDINGS[name].get("renewable"):
                renewable += BUILDINGS[name].get("energyProduction", 0) * count
        return renewable * 100 // production

# Kasvattaa tai vähentää asukaslukua, riippuen vapaista asuinpaikoista, onnellisuudesta ja ruoan määrästä.

    def updatePopulation(self):
        housingCapacity = self.getTotal("housing")

        if housingCapacity > self.resources.population and self.sustainability.happiness >= HAPPINESS_GROWTH_MIN and self.resources.food > 0:
            growth = max(1, int(self.resources.population * GROWTH_RATE))
            newPopulation = self.resources.population + growth
            self.resources.population = min(newPopulation, housingCapacity)

        elif self.sustainability.happiness < HAPPINESS_DECLINE_MIN:
            decline = max(1, int(self.resources.population * DECLINE_RATE_UNHAPPINESS))
            newPopulation = self.resources.population - decline
            self.resources.population = max(0, newPopulation)

        elif self.resources.food <= 0:
            decline = max(1, int(self.resources.population * DECLINE_RATE_HUNGER))
            newPopulation = self.resources.population - decline
            self.resources.population = max(0, newPopulation)

# Rakennusmetodi jolla pelaaja voi rakentaa uuden rakennuksen jos se on olemassa ja on tarpeeksi rahaa
# (tarkistaa onko annettu rakennus BUILDINGS sanakirjassa)

    def build(self, name):
        if name not in BUILDINGS:
            return f"{name} ei ole olemassa, kokeile uudestaan."
        
        cost = BUILDINGS[name]["cost"]

        if self.resources.money < cost:
            return f"Ei tarpeeksi rahaa, tarvitset {cost - self.resources.money} €"
        
        self.buildings[name] = self.buildings.get(name, 0) + 1
        self.resources.money -= cost
        return f"Rakensit rakennuksen {name}, rahaa jäljellä: {self.resources.money}"

# Palauttaa tämän hetkisen tilanteen (resurssit ja kestävyystavoitteet)

    def getStatus(self):
        r, s, b = self.resources, self.sustainability, self.buildings
        return (
            f"\nVuosi: {self.year}\n"
            f"\n"
            f"RESURSSIT\n"
            f"Asukkaat: {r.population}/{b["talo"] * BUILDINGS["talo"]["housing"]}\n"
            f"Raha: {r.money} €\n"
            f"Ruoka: {r.food}\n"
            f"\n"
            f"KESTÄVYYSTAVOITTEET\n"
            f"Puhdas vesi: {s.cleanWater}%\n"
            f"Uusiutuva energia: {s.renewableShare}%\n"
            f"Koulutus: {s.education}%\n"
            f"Tasa-arvo: {s.equality}%\n"
            f"Ympäristö: {s.environment}%\n"
            f"Onnellisuus: {s.happiness}%"
        )

# Palauttaa tämänhetkiset rakennukset ja niiden kokonaisvaikutuksen per rakennustyyppi

    def getBuildings(self):
        lines = []
        for name, count in self.buildings.items():
            b = BUILDINGS[name]
            lines.append(f"{30 * "-"}\n{name.upper()} ({count} kpl)")
            if b["housing"] != 0:
                lines.append(f"Asukaspaikkojen määrä yht: {b["housing"] * count}")
            if b["upkeep"] != 0:
                lines.append(f"Ylläpidon kustannus yht: -{b["upkeep"] * count} €")
            if b["foodProduction"] != 0:
                lines.append(f"Ruoan tuotanto yht: {b["foodProduction"] * count}")
            if b["cleanWater"] != 0:
                lines.append(f"Veden tuotanto yht: {b["cleanWater"] * count}")
            if b["energyProduction"] != 0:
                lines.append(f"Energian tuotanto yht: {b["energyProduction"] * count}")
            if b["renewable"] == True:
                lines.append(f"Uusiutuva")
            if b["education"] != 0:
                lines.append(f"Koulutus yht: {b["education"] * count}")
            if b["happiness"] != 0:
                lines.append(f"Onnellisuus yht: {b["happiness"] * count}")
            if b["equality"] != 0:
                lines.append(f"Tasa-arvo yht: {b["equality"] * count}")
            if b["environment"] != 0:
                lines.append(f"Ympäristön vaikutus: {b["environment"] * count}")
            lines.append("\n")
        return "\n".join(lines)

# Palauttaa vuosittaisen muutoksen yhteensä (rakennuksien tuotto, kulutus + rappeutuminen kestävyystavoitteista)

    def getSpending(self):
        lines = []
        lines.append(f"\nVuosittainen muutos yhteensä\n-------------------")

        # Resurssit
        moneyChange = self.resources.getIncome() - self.getTotal("upkeep")
        foodChange = self.getTotal("foodProduction") - self.resources.getFoodConsumption()
        energyChange = self.getTotal("energyProduction") - self.resources.getEnergyConsumption()

        lines.append(f"Raha: {moneyChange:+} €/vuosi")
        lines.append(f"Ruoka: {foodChange:+}/vuosi")
        lines.append(f"Energia: {energyChange:+}/vuosi")

        # Kestävyystavoitteet: rakennusten vaikutus + rapautuminen
        lines.append("\nKestävyystavoitteet")
        lines.append(f"Puhdas vesi: {self.getTotal('cleanWater') + DECAY['cleanWater']:+}%/vuosi")
        lines.append(f"Koulutus: {self.getTotal('education') + DECAY['education']:+}%/vuosi")
        lines.append(f"Tasa-arvo: {self.getTotal('equality') + DECAY['equality']:+}%/vuosi")
        lines.append(f"Ympäristö: {self.getTotal('environment') + DECAY['environment']:+}%/vuosi")
        lines.append(f"Onnellisuus: {self.getTotal('happiness') + DECAY['happiness']:+}%/vuosi")

        if energyChange < 0:
            lines.append("\nVaroitus: energia ei riitä, onnellisuus tippuu -5 ja tasa-arvo -2 lisää!")

        return "\n".join(lines)

# Palauttaa listan rakennuksista, joita pystyy rakentamaan. (Sanakirja rakennuksista erissä tiedostossa)

    def getBuildingsList(self):
        lines = ["Tässä lista rakennuksista joita voit rakentaa"]
        for building in BUILDINGS:
            b = BUILDINGS[building]
            lines.append(f"\n{building.upper()}")
            lines.append(f"Hinta: {b["cost"]} €")
            lines.append(f"Ylläpito: {b["upkeep"]} €/v")
            if b["housing"] != 0:
                lines.append(f"Asuntoja: {b["housing"]}")
            if b["foodProduction"] != 0:
                lines.append(f"Ruoka: {b["foodProduction"]}")
            if b["cleanWater"] != 0:
                lines.append(f"Puhdas vesi: {b["cleanWater"]}")
            if b["education"] != 0:
                lines.append(f"Koulutus: {b["education"]}")
            if b["energyProduction"] != 0:
                lines.append(f"Energiaa: {b["energyProduction"]}")
            if b["environment"] != 0:
                lines.append(f"Ympäristö: {b["environment"]}")
            if b["happiness"] != 0:
                lines.append(f"Onnellisuus: {b["happiness"]}")
            if b["equality"] != 0:
                lines.append(f"Tasa-arvo: {b["equality"]}")
            if b["renewable"]:
                lines.append("Uusiutuva")
        return "\n".join(lines)