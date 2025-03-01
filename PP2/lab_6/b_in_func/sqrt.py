# Program to calculate square root after delay
import math  # For sqrt function
import time  # For sleep function

number = 25100  # Sample number
delay = 2123    # Delay in milliseconds

print(f"Calculating square root of {number}...")
time.sleep(delay / 1000)  # Convert ms to seconds and wait
result = math.sqrt(number)  # Calculate square root

print(f"Square root of {number} after {delay} milliseconds is {result}")
# Output: Square root of 25100 after 2123 milliseconds is 158.42979517754858