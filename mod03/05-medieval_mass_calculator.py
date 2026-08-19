talent = float(input("Kirjoita paino leivisköinä: "))
pound = float(input("Kirjoita paino nauloina: "))
lot = float(input("Kirjoita paino luoteina: "))

## Initialize medieval weights accordingly

lot_weight = 13.3
pound_weight = lot_weight * 32
talent_weight = pound_weight * 20

## Calculate the weights

lots = lot_weight * lot
pounds = pound_weight * pound
talents = talent_weight * talent

## Calculate the total mass and turn them into kg and g

total_mass = lots + pounds + talents
mass_kg = int(total_mass / 1000)
mass_g = total_mass - (mass_kg * 1000)

print(f'Kokonaismassa nykymittojen mukaan: {mass_kg} kilogrammaa ja {mass_g:.2f} grammaa.')