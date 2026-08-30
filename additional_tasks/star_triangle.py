triangle_size = int(input("Anna kolmion korkeus: "))


for i in range(triangle_size):
    string = "*"
    space = " "
    print(f"{(space * (triangle_size - i)) + (string * i * 2) + "*"}")