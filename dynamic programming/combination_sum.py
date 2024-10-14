def combination_sum(nums, target):
    n = len(nums)
    results = []

    def solve(idx, target, res):
        if target < 0:
          return
        
        if target == 0:
            results.append(res[:])
            return
          
        if idx == -1:
            return

        
        res.append(nums[idx])
        solve(idx, target - nums[idx], res)
        res.pop()
        solve(idx - 1, target, res)
            
    solve(n - 1, target, [])
    
    return results