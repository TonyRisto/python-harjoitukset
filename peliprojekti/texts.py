ENERGY_PER_CAPITA = 2

FOOD_PER_CAPITA = 1

INCOME_PER_CAPITA = 1000

GROWTH_RATE = 0.03

DECLINE_RATE_UNHAPPINESS = 0.05

DECLINE_RATE_HUNGER = 0.10

HAPPINESS_GROWTH_MIN = 50

HAPPINESS_DECLINE_MIN = 30

commands = "\nrakennukset\ntilanne\nkulutus\nseuraava (pelissä vuosi eteenpäin)\ntallenna\npaavalikko\n"

BUILDINGS = {
    "talo": {"cost": 50000, "housing": 10, "upkeep": 500},
    "maatila": {"cost": 30000, "foodProduction": 25, "environment": -2, "upkeep": 1000},
    "vesitorni": {"cost": 45000, "cleanWater": 10, "upkeep": 1000},
    "koulu": {"cost": 100000, "education": 8, "upkeep": 4000},
    "hakevoimalaitos": {"cost": 60000,  "energyProduction": 120, "environment": -2, "upkeep": 3000},
    "aurinkopaneeli": {"cost": 40000,  "energyProduction": 30, "environment": 2, "renewable": True, "upkeep": 200},
    "tuulimylly": {"cost": 80000,  "energyProduction": 80, "environment": 2, "renewable": True, "upkeep": 800},
    "biolampolaitos": {"cost": 90000,  "energyProduction": 100, "environment": -2, "renewable": True, "upkeep": 2500},
    "puisto": {"cost": 25000,  "environment": 3, "happiness": 3, "upkeep": 500},
    "terveysasema": {"cost": 70000,  "happiness": 5, "upkeep": 3000},
    "seurakuntatalo": {"cost": 50000, "equality": 4, "happiness": 2, "upkeep": 1500}
    }