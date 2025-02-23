def check_ab(string):
    # Check if string is empty
    if not string:
        return False
    
    # Make sure first character is 'a'
    if string[0] != 'a':
        return False
    
    # Loop through rest of string to check for only 'b's
    for char in string[1:]:
        if char != 'b':
            return False
    
    # If we get here, string matches pattern
    return True

# List of test words to check
test_words = ['a', 'ab', 'abb', 'abbb', 'b', 'ba', 'abc', '']

# Test each word and print result
for word in test_words:
    result = check_ab(word)
    print(f"{word}: {'Yes' if result else 'No'}")