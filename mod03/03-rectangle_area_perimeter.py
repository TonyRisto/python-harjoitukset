rectangle_base_input = input("Kirjoita suorakulmion kannan pituus senttimetreinä: ")
rectangle_height_input = input("Kirjoita suorakulmion korkeus senttimetreinä: ")

rectangle_base = float(rectangle_base_input)
rectangle_height = float(rectangle_height_input)

rectangle_base_two = rectangle_base * 2
rectangle_height_two = rectangle_height * 2

perimeter = rectangle_base_two + rectangle_height_two
area = rectangle_base * rectangle_height

print(f"Suorakulmion pinta-ala on: {area} cm^2")
print(f"Suorakulmion piiri on: {perimeter} cm")