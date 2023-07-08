def sum_of_squares(n):
    # Calculate the sum of the squares of the first n natural numbers
    return sum(i**2 for i in range(1, n+1))

def square_of_sum(n):
    # Calculate the square of the sum of the first n natural numbers
    return sum(range(1, n+1))**2

# Set the value of n to 100
n = 100

# Calculate the difference between the sum of squares and square of the sum
difference = square_of_sum(n) - sum_of_squares(n)

print("The difference between the sum of squares and square of the sum for the first", n, "natural numbers is:", difference)
