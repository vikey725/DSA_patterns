def climb_stairs(nums):
    if nums <= 1:
        return 1
    
    return climb_stairs(nums - 1) + climb_stairs(nums - 2)

def climb_stairs(nums):
    dp = [0 for _ in range(nums + 1)]
    dp[0] = dp[1] = 1
    
    for i in range(2, nums + 1):
      dp[i] = dp[i - 1] + dp[i - 2]
      
    return dp[nums]
    