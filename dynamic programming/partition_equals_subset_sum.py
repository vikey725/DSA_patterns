def can_partition_array(nums):
    n = len(nums)
    total = sum(nums)

    if total % 2 != 0:
        return False
    
    def solve(idx, target):
        if idx == 0:
            if target - nums[idx] != 0:
                return False
            
        if target - nums[idx] == 0:
            return True

        not_take = solve(idx - 1, target)
        take = False
        if nums[idx] <= target:
            take = solve(idx - 1, target - nums[idx])

        return take or not_take
    
    return solve(n - 1, total // 2)

def can_partition_array(nums):
    n = len(nums)
    total = sum(nums)
    visited = {}

    if total % 2 != 0:
        return False
    
    def solve(idx, target):
        if idx == 0:
            if target - nums[idx] != 0:
                return False
            
        if target - nums[idx] == 0:
            return True
        
        if (idx, target) in visited:
            return visited[(idx, target)]

        not_take = solve(idx - 1, target)
        take = False
        if nums[idx] <= target:
            take = solve(idx - 1, target - nums[idx])

        visited[(idx, target)] = take or not_take

        return take or not_take
    
    return solve(n - 1, total // 2)