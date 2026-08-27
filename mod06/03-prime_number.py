number = input("Anna kokonaisluku (paina s lopettaaksesi): ")
primes = []

while number != "s":
    number = int(number)
    for i in range(number):
        i += 1
        is_prime = number % i
        if is_prime == 0:
            primes.append(is_prime)

    if len(primes) != 2:
        print(f"{number} ei ole alkuluku")
    if len(primes) == 2:
        print(f"{number} on alkuluku")
    primes.clear()
    number = input("Anna kokonaisluku (paina s lopettaaksesi): ")