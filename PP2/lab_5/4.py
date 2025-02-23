def find_upper_lower_sequences(string):
    # List to store valid sequences
    valid_sequences = []
    
    # Current sequence being built
    current = ''
    
    # Loop through each character in the string
    for i in range(len(string)):
        # If first char of sequence, must be uppercase
        if not current and string[i].isupper():
            current = string[i]
        
        # If we have an uppercase start, check for lowercase
        elif current and string[i].islower():
            current += string[i]
        
        # If we hit an uppercase and have a sequence, save it
        elif current and string[i].isupper():
            if len(current) > 1:  # Must have at least one lowercase
                valid_sequences.append(current)
            current = string[i]
        
        # If non-letter or wrong case, reset
        else:
            if current and len(current) > 1:
                valid_sequences.append(current)
            current = ''
    
    # Check if last sequence is valid
    if current and len(current) > 1:
        valid_sequences.append(current)
    
    return valid_sequences

# Test cases to try
test_strings = [
    'HelloWorld',
    'AcatBdog',
    'Xyz',
    'HELLOworld',
    'Cat123Dog',
    'AbCdEf',
    'Z',
    'lowerUPPER'
]

# Loop through tests and print results
for test in test_strings:
    result = find_upper_lower_sequences(test)
    if result:
        print(f"{test}: Found {result}")
    else:
        print(f"{test}: No matches")