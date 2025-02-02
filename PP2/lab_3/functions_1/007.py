def spy_game(nums):
    code = [0, 0, 7]
    
    for num in nums:
        # If the current number matches the first number in the sequence,
        # remove that number from the sequence.
        #if code is here to to check if numbers are still left in code sequence
        if code and num == code[0]:
            code.pop(0)
    
    # code will be empty If we've found all the numbers in the sequence and we return True.
    return len(code) == 0 #len(code) == 0 returns True so iverall function also returns True

print(spy_game([1, 2, 4, 0, 0, 7, 5]))  
print(spy_game([1, 0, 2, 4, 0, 5, 7]))  
print(spy_game([1, 7, 2, 0, 4, 5, 0]))  
