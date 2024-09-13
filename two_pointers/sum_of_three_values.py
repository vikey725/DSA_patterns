def find_sum_of_three(nums, target):
    nums.sort()
    
    n = len(nums)
    for s in range(n - 2):
        l, r = s + 1, n - 1

        while l < r:
            cur_sum = nums[s] + nums[l] + nums[r]
            if cur_sum == target:
                return True
            elif cur_sum > target:
                r -= 1
            else:
                l += 1
    
    return False

"""
    TC: O(n * n)
    SC: O(1)
"""
