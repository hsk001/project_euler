def gcd(a, b):
    # Calculate the greatest common divisor (GCD) using Euclid's algorithm
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    # Calculate the least common multiple (LCM) using the GCD
    return (a * b) // gcd(a, b)

def smallest_multiple(limit):
    # Calculate the LCM iteratively for all numbers from 1 to the limit
    result = 1
    for i in range(1, limit + 1):
        result = lcm(result, i)
    return result

# Set the limit to 20
limit = 20

# Calculate and print the smallest positive number divisible by all numbers from 1 to 20
smallest = smallest_multiple(limit)
print(f"The smallest positive number divisible by all numbers from 1 to {limit} is: {smallest}")
