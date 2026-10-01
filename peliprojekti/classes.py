from texts import (
    BUILDINGS,
    ENERGY_PER_CAPITA,
    FOOD_PER_CAPITA,
    INCOME_PER_CAPITA,
    GROWTH_RATE,
    DECLINE_RATE_UNHAPPINESS,
    DECLINE_RATE_HUNGER,
    HAPPINESS_GROWTH_MIN,
    HAPPINESS_DECLINE_MIN
)

class Resources:
    def __init__(self):
        self.population = 100
        self.money = 500000
        self.food = 500

    def getEnergyConsumption(self):
        return self.population * ENERGY_PER_CAPITA

    def getFoodConsumption(self):
        return self.population * FOOD_PER_CAPITA

    def getIncome(self):
        return self.population * INCOME_PER_CAPITA



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

class GameState:
    def __init__(self):
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

    def advanceYear(self):
        self.resources.money += self.resources.getIncome() - self.getTotal("upkeep")
        self.resources.food += self.getTotal("foodProduction") - self.resources.getFoodConsumption()
        energyBalance = self.getTotal("energyProduction") - self.resources.getEnergyConsumption()
        self.sustainability.renewableShare = self.getRenewableShare()

        if energyBalance < 0:
            self.sustainability.change("happiness", -5)
            self.sustainability.change("equality", -2)

        for name, count in self.buildings.items():
            for key, value in BUILDINGS[name].items():
                if key in ("cleanWater", "education", "equality", "environment", "happiness"):
                    self.sustainability.change(key, value * count)
        
        self.updatePopulation()
        self.year += 1

    def getTotal(self, key):
        total = 0
        for name, count in self.buildings.items():
            total += BUILDINGS[name].get(key, 0) * count
        return total

    def getRenewableShare(self):
        production = self.getTotal("energyProduction")
        if production == 0:
            return 0
        renewable = 0
        for name, count in self.buildings.items():
            if BUILDINGS[name].get("renewable"):
                renewable += BUILDINGS[name].get("energyProduction", 0) * count
        return renewable * 100 // production

    def updatePopulation(self):
        housingCapacity = self.getTotal("housing")

        if housingCapacity > self.resources.population and self.sustainability.happiness > HAPPINESS_GROWTH_MIN and self.resources.food > 0:
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

    def build(self, name):
        if name not in BUILDINGS:
            return f"{name} ei ole olemassa, kokeile uudestaan."
        
        cost = BUILDINGS[name]["cost"]

        if self.resources.money < cost:
            return f"Ei tarpeeksi rahaa, tarvitset {cost - self.resources.money}"
        
        self.buildings[name] = self.buildings.get(name, 0) + 1
        self.resources.money -= cost
        return f"Ostit rakennuksen {name}"

    def getStatus(self):
        lines = []
        lines.append(f"Vuosi: {self.year}\n-------------------")
        lines.append(f"Resurssit")
        lines.append(f"Asukkaat: {self.resources.population}")
        lines.append(f"Raha: {self.resources.money} €")
        lines.append(f"Ruoka: {self.resources.food}")
        lines.append(f"Kestävyystavoitteet\n-------------------")
        lines.append(f"Puhdas vesi: {self.sustainability.cleanWater}%")
        lines.append(f"Uusiutuva energia: {self.sustainability.renewableShare}%")
        lines.append(f"Koulutus: {self.sustainability.education}%")
        lines.append(f"Tasa-arvo: {self.sustainability.equality}%")
        lines.append(f"Ympäristö: {self.sustainability.environment}%")
        lines.append(f"Onnellisuus: {self.sustainability.happiness}%")
        lines.append(f"-------------------\nRakennukset")
        for name, count in self.buildings.items():
            lines.append(f"{name}: ({count} kpl)")
        return "\n".join(lines)

    def getBuildingsList(self):
        buildings = []
        for name in BUILDINGS:
            buildings.append(f"{name}: hinta {BUILDINGS[name]["cost"]} €")
        return "\n".join(buildings)