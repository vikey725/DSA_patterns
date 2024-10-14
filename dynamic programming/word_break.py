def word_break(s, word_dict):
    
    def solve(idx):
        if idx == -1:
            return True


        for j in range(idx, -1, -1):
            sub = s[j:idx + 1]

            if sub in word_dict and solve(j - 1):
                return True
        
        return False
    
    n = len(s)    
    return solve(n - 1)

def word_break(s, word_dict):
    dp = {}
    def solve(idx):
        if idx == -1:
            return True

        if idx in dp:
            return dp[idx]

        for j in range(idx, -1, -1):
            sub = s[j:idx + 1]

            if sub in word_dict and solve(j - 1):
                dp[idx] = True
                return True
            dp[idx] = False
        
        return False
    return solve(len(s) - 1)