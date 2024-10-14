def count_palindromic_substrings(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    count = 0

    for i in range(n):
        dp[i][i] = True
        count += 1

    for i in range(1, n):
        dp[i - 1][i] = (s[i - 1] == s[i])
        count += dp[i - 1][i]

    for str_len in range(3, n + 1):
        i = 0
        for j in range(str_len - 1, n):
            dp[i][j] = dp[i + 1][j - 1] and (s[i] == s[j])
            count += dp[i][j]
            i += 1

    return count