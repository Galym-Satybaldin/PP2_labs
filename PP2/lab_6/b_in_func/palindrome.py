# Program to check if string is palindrome
def is_palindrome(text):
    # Convert to lowercase and remove spaces
    clean_text = ''.join(text.lower().split())
    # Compare with its reverse using slicing
    return clean_text == clean_text[::-1]

# Test cases
word1 = "Racecar"
word2 = "Hello"

print(f"Is '{word1}' a palindrome? {is_palindrome(word1)}")  # True
print(f"Is '{word2}' a palindrome? {is_palindrome(word2)}")  # False