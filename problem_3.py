def calculate_prime_factors(number):
    prime_factors = []
    divisor = 2

    while divisor <= number:
        if number % divisor == 0:
            prime_factors.append(divisor)
            number /= divisor
        else:
            divisor += 1

    return prime_factors

# Define the number for which prime factors are to be calculated
number = 600851475143

# Calculate and print the prime factors
prime_factors = calculate_prime_factors(number)
print("Lrgest Prime factor of", number, "is:", max(prime_factors))
