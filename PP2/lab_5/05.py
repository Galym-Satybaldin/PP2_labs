def check_a_anything_b(string):
    # Check if string is too short (need at least 'a' and 'b')
    if len(string) < 2:
        return False
    
    # First character must be 'a'
    if string[0] != 'a':
        return False
    
    # Last character must be 'b'
    if string[-1] != 'b':
        return False
    
    # If it passes these checks, it's a match
    return True

# Test cases to try
test_strings = [
    'ab',
    'axb',
    'a123b',
    'aXyZb',
    'b',
    'ba',
    'abc',
    'a',
    'a_b'
]

# Loop through tests and print results
for test in test_strings:
    result = check_a_anything_b(test)
    print(f"{test}: {'Yes' if result else 'No'}")