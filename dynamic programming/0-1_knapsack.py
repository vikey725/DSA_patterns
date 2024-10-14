# Recirsion
def find_max_knapsack_profit(capacity, weights, values):
    n = len(weights)
    tracker = {}

    def solve(i, capacity):
        if i == 0:
            if capacity >= weights[i]:
                return values[i]
            return 0

        not_take = solve(i - 1, capacity)
        take = -1e9
        if capacity >= weights[i]:
            take = values[i] + solve(i - 1, capacity - weights[i])

        return max(take, not_take)
    
    return solve(n - 1, capacity)

# Memoization
def find_max_knapsack_profit(capacity, weights, values):
    n = len(weights)
    tracker = {}

    def solve(i, capacity):
        if i == 0:
            if capacity >= weights[i]:
                return values[i]
            return 0
        
        if (i, capacity) in tracker:
            return tracker[(i, capacity)]

        not_take = solve(i - 1, capacity)
        take = -1e9
        if capacity >= weights[i]:
            take = values[i] + solve(i - 1, capacity - weights[i])

        tracker[(i, capacity)] = max(take, not_take)
        return tracker[(i, capacity)]
    
    return solve(n - 1, capacity)

# Tabulation
def find_max_knapsack_profit(capacity, weights, values):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n)]

    def solve():
        for w in range(weights[0], capacity + 1):
            dp[0][w] = values[0]

        for i in range(1, n):
            for w in range(capacity + 1):
                not_take = dp[i - 1][w]
                take = -1e9
                if w >= weights[i]:
                    take = values[i] + dp[i - 1][w - weights[i]]

                dp[i][w] = max(take, not_take)

        return dp[n - 1][capacity]
    
    return solve()

res = find_max_knapsack_profit(6, [1,2,3,5], [1,5,4,8])
print(res)
