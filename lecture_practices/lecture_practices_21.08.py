wall_height = float(input("Anna seinän korkeus metreinä: "))
wall_width = float(input("Anna seinän leveys metreinä: "))
paint_per_m2 = float(input("Anna monta neliömetriä seinää voi maalata litralla maalia: "))

## Seinän pinta-ala
wall_area = wall_height * wall_width
paint_liter_per_m2 = wall_area / paint_per_m2

print(f'Seinän pinta-ala on: {wall_area} m^2')
print(f'Maalia tarvitaan: {paint_liter_per_m2}l')