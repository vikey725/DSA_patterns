def first_val_higher_than_target(nums, target):
    left, right = 0, len(nums) - 1
    if target >= nums[right]:
        return right + 1
    
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > target:
            right = mid
        else:
            left = mid + 1

    return left

def first_val_lower_than_target(nums, target):
    left, right = 0, len(nums) - 1

    ans = -1

    if target > nums[right]:
        return right
    
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] >= target:
            right = mid - 1
        else:
            ans = mid
            left = mid + 1
        # input('...')

    return ans


nums = [100, 103, 107, 110, 114, 117, 119, 123]
targets = [100, 102, 115, 117, 120, 124]
print('\nHigher:')
for target in targets:
    res = first_val_higher_than_target(nums, target)
    print(target, res)

print("\nLower:")
for target in targets:
    res = first_val_lower_than_target(nums, target)
    print(target, res)