def number_list(numbers_list):
    for i in numbers_list:
        print(i)
    i = len(numbers_list) - 1
    while i >= 0:
        if numbers_list[i] % 2 != 0:
            numbers_list.pop(i)
        i -= 1


        

numbers = []
number = input("Anna numero (paina enter lopettaaksesi): ")

while number != "":
    number = int(number)
    numbers.append(number)
    number = input("Anna numero: ")

print(number_list(numbers))
print(number_list(numbers))