def find_pythagorean_triplet(target_sum):
    for a in range(1, target_sum // 3):
        for b in range(a + 1, (target_sum - a) // 2):
            c = target_sum - a - b
            if a**2 + b**2 == c**2:
                return a, b, c
    return None

# Set the target sum to 1000
target_sum = 1000

# Find the Pythagorean triplet
triplet = find_pythagorean_triplet(target_sum)

if triplet:
    a, b, c = triplet
    product = a * b * c
    print("The Pythagorean triplet for which a + b + c =", target_sum, "is:", triplet)
    print("The product of the triplet is:", product)
else:
    print("No Pythagorean triplet found for which a + b + c =", target_sum)
