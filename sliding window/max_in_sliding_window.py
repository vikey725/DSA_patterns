from collections import deque

def clean_up(current_window, i, nums):
    while current_window and nums[current_window[-1]] <= nums[i]:
        current_window.pop()

def find_max_sliding_window(nums, w):
    current_window = deque()
    result = []

    for i in range(w):
        clean_up(current_window, i, nums)
        current_window.append(i)
    # print(list(current_window))
    result.append(nums[current_window[0]])

    for i in range(w, len(nums)):
        clean_up(current_window, i, nums)
        while current_window and current_window[0] <= i - w:
            current_window.popleft()
        current_window.append(i)

        result.append(nums[current_window[0]])

    return result

"""
    TC: O(n)
    SC: O(w)
"""