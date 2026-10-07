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
    "talo": {
        "cost": 50000, "upkeep": 500, "renewable": False,
        "housing": 10, "foodProduction": 0, "cleanWater": 0, "education": 0,
        "energyProduction": 0, "environment": 0, "happiness": 0, "equality": 0,
    },
    "maatila": {
        "cost": 30000, "upkeep": 1000, "renewable": False,
        "housing": 0, "foodProduction": 25, "cleanWater": 0, "education": 0,
        "energyProduction": 0, "environment": -2, "happiness": 0, "equality": 0,
    },
    "vesitorni": {
        "cost": 45000, "upkeep": 1000, "renewable": False,
        "housing": 0, "foodProduction": 0, "cleanWater": 10, "education": 0,
        "energyProduction": 0, "environment": 0, "happiness": 0, "equality": 0,
    },
    "koulu": {
        "cost": 100000, "upkeep": 4000, "renewable": False,
        "housing": 0, "foodProduction": 0, "cleanWater": 0, "education": 8,
        "energyProduction": 0, "environment": 0, "happiness": 0, "equality": 0,
    },
    "hakevoimalaitos": {
        "cost": 60000, "upkeep": 3000, "renewable": False,
        "housing": 0, "foodProduction": 0, "cleanWater": 0, "education": 0,
        "energyProduction": 120, "environment": -2, "happiness": 0, "equality": 0,
    },
    "aurinkopaneeli": {
        "cost": 40000, "upkeep": 200, "renewable": True,
        "housing": 0, "foodProduction": 0, "cleanWater": 0, "education": 0,
        "energyProduction": 30, "environment": 2, "happiness": 0, "equality": 0,
    },
    "tuulimylly": {
        "cost": 80000, "upkeep": 800, "renewable": True,
        "housing": 0, "foodProduction": 0, "cleanWater": 0, "education": 0,
        "energyProduction": 80, "environment": 2, "happiness": 0, "equality": 0,
    },
    "biolampolaitos": {
        "cost": 90000, "upkeep": 2500, "renewable": True,
        "housing": 0, "foodProduction": 0, "cleanWater": 0, "education": 0,
        "energyProduction": 100, "environment": -2, "happiness": 0, "equality": 0,
    },
    "puisto": {
        "cost": 25000, "upkeep": 500, "renewable": False,
        "housing": 0, "foodProduction": 0, "cleanWater": 0, "education": 0,
        "energyProduction": 0, "environment": 3, "happiness": 3, "equality": 0,
    },
    "terveysasema": {
        "cost": 70000, "upkeep": 3000, "renewable": False,
        "housing": 0, "foodProduction": 0, "cleanWater": 0, "education": 0,
        "energyProduction": 0, "environment": 0, "happiness": 5, "equality": 0,
    },
    "seurakuntatalo": {
        "cost": 50000, "upkeep": 1500, "renewable": False,
        "housing": 0, "foodProduction": 0, "cleanWater": 0, "education": 0,
        "energyProduction": 0, "environment": 0, "happiness": 2, "equality": 4,
    },
}

DECAY = {
    "cleanWater": -3,
    "education": -2,
    "equality": -2,
    "environment": -1,
    "happiness": -1,
}