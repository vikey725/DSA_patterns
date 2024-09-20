def smallest_missing_positive_integer(nums):
    n = len(nums)
    i = 0

    while i < n:
        val = nums[i]

        if 1 <= val <= n and nums[val - 1] != nums[i]:
            nums[val - 1], nums[i] = nums[i], nums[val - 1]
        else:
            i += 1

    for i in range(n):
        if i + 1 != nums[i]:
            return i + 1
    return n + 1


nums = [0,-1,-2,-3,5]
res = smallest_missing_positive_integer(nums)
print(res)