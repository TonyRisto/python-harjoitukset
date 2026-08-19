import math

circle_radius_input = input("Anna säteen pituus senttimetreinä: ")
circle_radius = float(circle_radius_input)

circle_area = math.pi * circle_radius**2

print(f"Ympyrän pinta-ala: {circle_area:.2f} cm^2")