def coin_change(coins, total):
    n = len(coins)

    def solve(idx, total):
        if idx == 0:
            if total % coins[idx] == 0:
                return total // coins[idx]
            return 1e9

        not_take = 0 + solve(idx - 1, total)

        take = 1e9
        if total >= coins[idx]:
            take = 1 + solve(idx, total - coins[idx])

        return min(take, not_take)
    
    res = solve(n - 1, total)
    if res >= 1e9:
        return -1
    return res

def coin_change(coins, total):
    n = len(coins)
    visited = {}

    def solve(idx, total):
        if idx == 0:
            if total % coins[idx] == 0:
                return total // coins[idx]
            return 1e9
        
        if (idx, total) in visited:
            return visited[(idx, total)]

        not_take = 0 + solve(idx - 1, total)

        take = 1e9
        if total >= coins[idx]:
            take = 1 + solve(idx, total - coins[idx])

        visited[(idx, total)] = min(take, not_take)

        return min(take, not_take)
    
    res = solve(n - 1, total)
    if res >= 1e9:
        return -1
    return res

#TODO Tabulation 