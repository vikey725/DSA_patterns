def house_robber(money):
    n = len(money)
    def solve(idx, start):
        if idx < start:
            return 0
        
        if idx in dp:
            return dp[idx]

        not_take = 0 + solve(idx - 1)

        take = money[idx] + solve(idx - 2)

        dp[idx] = max(take, not_take)

        return max(take, not_take)
    
    dp = {}
    include_first = solve(n - 2, 0)
    dp = {}
    include_last = solve(n - 1, 1)

    return max(include_first, include_last)