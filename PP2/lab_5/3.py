def find_letter_sequences(string):
    # Split the string at underscores
    parts = string.split('_')
    
    # List to store valid sequences
    valid_sequences = []
    
    # Need at least 2 parts (one underscore) to have a sequence
    if len(parts) < 2:
        return valid_sequences
    
    # Check each pair of parts
    for i in range(len(parts) - 1):
        # Get current and next part
        current = parts[i]
        next_part = parts[i + 1]
        
        # Both parts must have only lowercase letters and not be empty
        if (current.islower() and next_part.islower() and 
            current and next_part and 
            current.isalpha() and next_part.isalpha()):
            # Combine parts with underscore if they match rules
            sequence = current + '_' + next_part
            valid_sequences.append(sequence)
    
    return valid_sequences

# Test cases to try
test_strings = [
    'hello_world',
    'abc_def_ghi',
    'HELLO_world',
    'cat_123_dog',
    'one_two_three',
    '_start',
    'end_',
    'a_b_c_d'
]

# Loop through tests and print results
for test in test_strings:
    result = find_letter_sequences(test)
    if result:
        print(f"{test}: Found {result}")
    else:
        print(f"{test}: No matches")