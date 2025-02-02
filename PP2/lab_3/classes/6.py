# Define a list of numbers.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# Define an anonymous lambda function that returns True if a number is prime.
# The lambda checks:
# - The number is greater than 1.
# - All numbers from 2 up to the square root of the number (inclusive) do not divide it evenly.
is_prime = lambda x: x > 1 and all(x % i != 0 for i in range(2, int(x ** 0.5) + 1))

# Use filter with the lambda to extract prime numbers.
prime_numbers = list(filter(is_prime, numbers))

# Print the list of prime numbers.
print("Prime numbers:", prime_numbers)
