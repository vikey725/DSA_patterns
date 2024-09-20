"""
    Given an array, nums, containing n distinct numbers in the range [0,n], return the only number in the range that is missing from the array.
"""

def find_missing_number(nums):
    n = len(nums)
    i = 0
    while i < n:
        val = nums[i]
        if val < n and val != i:
            nums[i], nums[val] = nums[val], nums[i]
        else:
            i += 1

    for i in range(n):
        if i != nums[i]:
            return i
    return n 