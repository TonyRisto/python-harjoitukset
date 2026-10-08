# Vakiot

ENERGY_PER_CAPITA = 2

FOOD_PER_CAPITA = 1

INCOME_PER_CAPITA = 900

GROWTH_RATE = 0.12

DECLINE_RATE_UNHAPPINESS = 0.05

DECLINE_RATE_HUNGER = 0.10

HAPPINESS_GROWTH_MIN = 50

HAPPINESS_DECLINE_MIN = 30

# Pelin sisäiset komennot

commands = "\nrakennukset\ntilanne\nkulutus\nseuraava (pelissä vuosi eteenpäin)\ntallenna\npaavalikko (huom! tallentamaton peli katoaa)\n"

# Sanakirja rakennuksista, jonka sisällä sanakirja jokaisen rakennuksen vaikutuksesta.

BUILDINGS = {
    "talo": {
        "cost": 40000, "upkeep": 500, "renewable": False,
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
        "cost": 100000, "upkeep": 10000, "renewable": False,
        "housing": 0, "foodProduction": 0, "cleanWater": 0, "education": 8,
        "energyProduction": 0, "environment": 0, "happiness": 0, "equality": 4,
    },
    "hakevoimalaitos": {
        "cost": 50000, "upkeep": 2500, "renewable": False,
        "housing": 0, "foodProduction": 0, "cleanWater": 0, "education": 0,
        "energyProduction": 120, "environment": -2, "happiness": 0, "equality": 0,
    },
    "aurinkopaneeli": {
        "cost": 40000, "upkeep": 400, "renewable": True,
        "housing": 0, "foodProduction": 0, "cleanWater": 0, "education": 0,
        "energyProduction": 40, "environment": 2, "happiness": 0, "equality": 0,
    },
    "tuulimylly": {
        "cost": 80000, "upkeep": 800, "renewable": True,
        "housing": 0, "foodProduction": 0, "cleanWater": 0, "education": 0,
        "energyProduction": 80, "environment": 2, "happiness": 0, "equality": 0,
    },
    "biolampolaitos": {
        "cost": 80000, "upkeep": 3500, "renewable": True,
        "housing": 0, "foodProduction": 0, "cleanWater": 0, "education": 0,
        "energyProduction": 100, "environment": -2, "happiness": 0, "equality": 0,
    },
    "puisto": {
        "cost": 30000, "upkeep": 1000, "renewable": False,
        "housing": 0, "foodProduction": 0, "cleanWater": 0, "education": 0,
        "energyProduction": 0, "environment": 3, "happiness": 1, "equality": 0,
    },
    "terveysasema": {
        "cost": 60000, "upkeep": 5000, "renewable": False,
        "housing": 0, "foodProduction": 0, "cleanWater": 0, "education": 0,
        "energyProduction": 0, "environment": 0, "happiness": 4, "equality": 2,
    },
    "seurakuntatalo": {
        "cost": 50000, "upkeep": 2000, "renewable": False,
        "housing": 0, "foodProduction": 0, "cleanWater": 0, "education": 0,
        "energyProduction": 0, "environment": 0, "happiness": 2, "equality": 4,
    },
}

# Vakiomäärät mitkä "rappeuttaa" kestävyysmittareita.

DECAY = {
    "cleanWater": -12,
    "education": -10,
    "equality": -2,
    "environment": -1,
    "happiness": -1,
}