def is_palindrome(number):
    # Convert number to string and check if it reads the same forwards and backwards
    return str(number) == str(number)[::-1]

largest_palindrome = 0

# Iterate over all possible products of two 3-digit numbers
for i in range(100, 1000):
    for j in range(i, 1000):
        product = i * j

        # Check if the product is a palindrome and greater than the current largest palindrome
        if is_palindrome(product) and product > largest_palindrome:
            largest_palindrome = product

print("The largest palindrome made from the product of two 3-digit numbers is:", largest_palindrome)
