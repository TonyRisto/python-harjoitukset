import math

circle_radius_string = input("Anna säteen pituus senttimetreinä: ")
circle_radius = float(circle_radius_string)

circle_area = math.pi * pow(circle_radius, 2)

print(f"Ympyrän pinta-ala: {circle_area:.2f}")