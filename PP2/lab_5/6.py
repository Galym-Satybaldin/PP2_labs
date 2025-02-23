def replace_with_colon(string):
    # New string to build with replacements
    new_string = ''
    
    # Loop through each character in the string
    for char in string:
        # Check if character is space, comma, or dot
        if char == ' ' or char == ',' or char == '.':
            new_string += ':'  # Replace with colon
        else:
            new_string += char  # Keep the original character
    
    return new_string

# Test cases to try
test_strings = [
    'hello world',
    'cat,dog',
    'this.is.a.test',
    'a b,c.d',
    'no-changes-here',
    '',
    'one two,three.four'
]

# Loop through tests and print results
for test in test_strings:
    result = replace_with_colon(test)
    print(f"Original: '{test}' -> Replaced: '{result}'")