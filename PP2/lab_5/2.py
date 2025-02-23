def check_a_and_bbs(string):
    # Check if string is empty
    if not string:
        return False
    
    # First character must be 'a'
    if string[0] != 'a':
        return False
    
    # Length must be 3 or 4 (1 for 'a' plus 2 or 3 'b's)
    if len(string) < 3 or len(string) > 4:
        return False
    
    # Check each character after 'a' is a 'b'
    for char in string[1:]:
        if char != 'b':
            return False
    
    # If all checks pass, string matches
    return True

# Test cases to try
test_words = ['ab', 'abb', 'abbb', 'abbbb', 'a', 'b', 'abc', '']

# Loop through tests and show results
for word in test_words:
    result = check_a_and_bbs(word)
    print(f"{word}: {'Yes' if result else 'No'}")