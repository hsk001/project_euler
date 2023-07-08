def is_prime(n):
    # Check if a number is prime
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_nth_prime(n):
    # Find the nth prime number
    count = 0
    num = 2
    while count < n:
        if is_prime(num):
            count += 1
        if count == n:
            return num
        num += 1

# Set the value of n to 10001
n = 10001

# Find the 10001st prime number
prime = find_nth_prime(n)

print("The", n, "prime number is:", prime)
