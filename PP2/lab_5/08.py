def split_at_uppercase(string):
    # List to store the split parts
    parts = []
    
    # Current word being built
    current = ''
    
    # Loop through each character in the string
    for char in string:
        # If character is uppercase and we have a word, start new part
        if char.isupper() and current:
            parts.append(current)
            current = char
        # Add character to current word
        else:
            current += char
    
    # Add the last part if there is one
    if current:
        parts.append(current)
    
    return parts

# Test cases to try
test_strings = [
    'HelloWorld',
    'XMLParser',
    'SplitAtUpper',
    'ABC',
    'lowercase',
    'OneTwoThree',
    '',
    'A'
]

# Loop through tests and print results
for test in test_strings:
    result = split_at_uppercase(test)
    print(f"Original: '{test}' -> Split: {result}")