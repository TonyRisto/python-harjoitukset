def list_sum(numbers_list):
    sum_list = sum(numbers_list)
    return sum_list

numbers = []
number = input("Anna numero (paina enter lopettaaksesi): ")

while number != "":
    number = int(number)
    numbers.append(number)
    number = input("Anna numero: ")

summed = list_sum(numbers)
print(f"Numeroiden summa: {summed}")