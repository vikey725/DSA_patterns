def min_sub_array_len(target, nums):
    s, e, n = 0, 0, len(nums)

    window_size = float('inf')
    current_sum = 0
    for e in range(n):
        current_sum += nums[e]

        while current_sum >= target: 
            window_size = min(e - s + 1, window_size)
            current_sum -= nums[s]
            s += 1
            
    if window_size != float('inf'):
        return window_size


    return 0

"""
    TC: O(n)
    SC: O(1)
"""