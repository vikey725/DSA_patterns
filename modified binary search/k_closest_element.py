def find_closest_elements(nums, k, target):
  left, right = 0, len(nums) - k
  while left < right:
    mid = (left + right) // 2
    if target - nums[mid] > nums[mid + k] - target:
      left = mid + 1
    else: 
      right = mid
  return nums[left: left + k]

"""
    TC: O(log n)
    SC: O(1)
"""