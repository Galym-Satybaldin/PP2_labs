def add_spaces_at_capitals(string):
    # New string to build with spaces
    result = ''
    
    # Loop through each character in the string
    for i in range(len(string)):
        # If it's uppercase and not the first character, add a space
        if string[i].isupper() and i > 0:
            result += ' ' + string[i]
        # Otherwise just add the character
        else:
            result += string[i]
    
    return result

# Test cases to try
test_strings = [
    'HelloWorld',
    'XMLParser',
    'ThisIsATest',
    'ABC',
    'lowercase',
    'OneTwoThree',
    '',
    'StartWithCap'
]

# Loop through tests and print results
for test in test_strings:
    result = add_spaces_at_capitals(test)
    print(f"Original: '{test}' -> Spaced: '{result}'")