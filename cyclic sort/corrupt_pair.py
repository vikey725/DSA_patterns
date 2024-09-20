def find_corrupt_pair(nums):
    n = len(nums)
    i = 0

    while i < n:
        val = nums[i]

        if i + 1 != val and val != nums[val - 1]:
            nums[val -1], nums[i] = nums[i], nums[val - 1]
        else:
            i += 1

    result = []
    for i in range(n):
        if i + 1 != nums[i]:
            return [i + 1, nums[i]]