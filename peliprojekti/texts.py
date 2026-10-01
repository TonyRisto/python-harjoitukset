ENERGY_PER_CAPITA = 2

FOOD_PER_CAPITA = 1

INCOME_PER_CAPITA = 1500

GROWTH_RATE = 0.03

DECLINE_RATE_UNHAPPINESS = 0.05

DECLINE_RATE_HUNGER = 0.10

HAPPINESS_GROWTH_MIN = 50

HAPPINESS_DECLINE_MIN = 30

instructions = "Pelaat peliä antamalla vastauksia terminaalissa näkyviin kysymyksiin. Jokainen vastauksesi vaikuttaa pelin lopputulokseen, joten kannattaa miettiä miten vastaat."

BUILDINGS = {
    "house": {"cost": 50000, "housing": 10, "upkeep": 500},
    "farm": {"cost": 30000, "food": 50, "environment": -2, "upkeep": 1000},
    "waterTower": {"cost": 45000, "cleanWater": 10, "upkeep": 1000},
    "school": {"cost": 100000, "education": 8, "upkeep": 4000},
    "peatPlant": {"cost": 60000,  "energyProduction": 120, "environment": -5, "upkeep": 3000},
    "solarPanel": {"cost": 40000,  "energyProduction": 30, "environment": 1, "renewable": True, "upkeep": 200},
    "windTurbine": {"cost": 80000,  "energyProduction": 80, "renewable": True, "upkeep": 800},
    "biomassPlant": {"cost": 90000,  "energyProduction": 100, "environment": -2, "upkeep": 2500},
    "park": {"cost": 25000,  "environment": 3, "happiness": 3, "upkeep": 500},
    "clinic": {"cost": 70000,  "happiness": 5, "upkeep": 3000},
    "communityHall": {"cost": 50000, "equality": 4, "happiness": 2, "upkeep": 1500}
    }