def word_break(s, word_dict):
    n = len(s)
    results = []
    def solve(idx, res):
        if idx == -1:
            results.append(" ".join(res[::-1]))
            return

        for j in range(idx, -1, -1):
            if s[j: idx + 1] in word_dict:
                res.append(s[j: idx + 1])
                solve(j - 1, res)
                res.pop()
    
    solve(n - 1, [])
    return results

results = word_break("raincoats" , ["rain","oats","coat","s","rains","oat","coats","c"])
print(results)

