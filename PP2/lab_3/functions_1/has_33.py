def has_33(nums):
    for i in range (len(nums)-1):
        if nums[i] == nums[i+1] == 3:
            return True
    return False

numbers = input()
nums = [int(num) for num in numbers.split()]
print (has_33(nums))


print (has_33([1,3,3]))
print (has_33([1,2,3,4]))
print (has_33([3,3,3,3]))