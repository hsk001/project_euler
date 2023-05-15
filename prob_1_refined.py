def sum_of_multiples(n, k):
    p = (n - 1) // k
    return k * p * (p + 1) // 2

sum = sum_of_multiples(1000, 3) + sum_of_multiples(1000, 5) - sum_of_multiples(1000, 15)

print("The sum of all the multiples of 3 or 5 below 1000 is:", sum)

