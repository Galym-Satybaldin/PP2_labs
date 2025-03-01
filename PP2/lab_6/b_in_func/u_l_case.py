# Program to count upper and lower case letters
text = "Hello PYTHON 123"  # Sample string

upper_count = sum(1 for char in text if char.isupper())  # Count uppercase
lower_count = sum(1 for char in text if char.islower())  # Count lowercase

print(f"String: {text}")
print(f"Uppercase letters: {upper_count}")  # Output: 6 (PYTHON)
print(f"Lowercase letters: {lower_count}")  # Output: 4 (ello)