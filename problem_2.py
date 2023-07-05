def sum_even_fibonacci(limit):
    # Initialize variables
    a, b = 0, 1
    sum_even = 0

    # Calculate Fibonacci sequence
    while a <= limit:
        if a % 2 == 0:
            sum_even += a
        a, b = b, a + b

    return sum_even

# Set the limit to four million (4,000,000)
limit = 4000000

# Calculate and print the sum of even-valued Fibonacci terms
sum_even = sum_even_fibonacci(limit)
print(f"The sum of even-valued Fibonacci terms below {limit} is: {sum_even}")