def find_tribonacci(n):
    if n == 0:
        return 0
    if n <= 2:
        return 1
    
    return find_tribonacci(n - 1) + find_tribonacci(n - 2) + find_tribonacci(n - 3)

def find_tribonacci(n):
    if n == 0:
      return 0
    if n <= 2:
      return 1
    dp = [0] * (n + 1)
    dp[1] = dp[2] = 1

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    
    return dp[n]

def find_tribonacci(n):
    if n == 0:
      return 0
    if n <= 2:
      return 1
    x, y, z = 0, 1, 1

    for i in range(3, n + 1):
        r = x + y + z
        x, y, z = y, z, r
    
    return r