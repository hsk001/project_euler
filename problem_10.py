import time

def sum_of_primes(limit):
    primes = [True] * limit
    primes[0] = primes[1] = False
    p = 2

    while p * p < limit:
        if primes[p]:
            for i in range(p * p, limit, p):
                primes[i] = False
        p += 1

    sum_primes = sum(i for i, is_prime in enumerate(primes) if is_prime)
    return sum_primes

limit = 2000000

start_time = time.time()
sum_primes = sum_of_primes(limit)
end_time = time.time()

execution_time = end_time - start_time

print("The sum of all prime numbers below", limit, "is:", sum_primes)
print("Execution time:", execution_time, "seconds")
