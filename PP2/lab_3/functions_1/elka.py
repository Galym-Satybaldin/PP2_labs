def hystogram(nums):
    numbers = [int (num) for num in nums.split()]

    for num in numbers:
        print (num * '*')

nums = input()
hystogram(nums)