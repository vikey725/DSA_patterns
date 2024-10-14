def num_of_decodings(decode_str):
    if decode_str[0] == '0':
        return 0
    
    n = len(decode_str)
    dp = [0 for _ in range(n + 1)]
    dp[0] = dp[1] = 1 
    for idx in range(2, n + 1):
        if 1 <= int(decode_str[idx - 1]) <= 26:
            dp[idx] = dp[idx - 1]

        if decode_str[idx - 2] != '0' and 1 <= int(decode_str[idx - 2: idx]) <= 26:
            dp[idx] += dp[idx - 2]

    return dp[n]
        

        
