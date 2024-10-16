def counting_bits(n):
    dp = [0] * (n + 1) # [0, 1, 1, 2, 1, 2, 2]

    for i in range(1, n + 1):
        dp[i] = dp[i // 2] if i % 2 == 0 else dp[i // 2] + 1

    return dp
    
    