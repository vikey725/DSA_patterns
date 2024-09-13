"""
    Given an array of positive numbers, nums, such that the values lie in the range [1, n], inclusive, and that there are n+1
    numbers in the array, find and return the duplicate number present in nums. There is only one repeated number in nums.
"""

def find_duplicate(nums):
    slow, fast = nums[0], nums[0]

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    slow = nums[0]

    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return fast

"""
    TC: O(n)
    SC: O(1)
"""