def rob(nums) -> int:
    n = len(nums)
    
    def solve(idx):
        if idx < 0:
            return 0

        not_take = 0 + solve(idx - 1)

        take = nums[idx] + solve(idx - 2)

        return max(take, not_take)
    
    return solve(n - 1)

def rob(nums) -> int:
    n = len(nums)
    dp = {}
    def solve(idx):
        if idx < 0:
            return 0
        
        if idx in dp:
            return dp[idx]

        not_take = 0 + solve(idx - 1)

        take = nums[idx] + solve(idx - 2)

        dp[idx] = max(take, not_take)

        return max(take, not_take)
    
    return solve(n - 1)