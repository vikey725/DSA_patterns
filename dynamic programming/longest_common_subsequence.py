def longest_common_subsequence(str1, str2):
    m, n = len(str1), len(str2)

    def solve(i, j):

        if i < 0 or j < 0:
            return 0

        if str1[i] == str2[j]:
            return 1 + solve(i - 1, j - 1)
        return 0 + max(solve(i - 1, j), solve(i, j - 1))
    
    return solve(m - 1, n - 1)

def longest_common_subsequence(str1, str2):
    m, n = len(str1), len(str2)
    visited = {}

    def solve(i, j):

        if i < 0 or j < 0:
            return 0
            
        if (i, j) in visited:
            return visited[(i, j)]

        if str1[i] == str2[j]:
            visited[(i, j)] = 1 + solve(i - 1, j - 1)
        else:
            visited[(i, j)] = 0 + max(solve(i - 1, j), solve(i, j - 1))
        
        return visited[(i, j)]
    
    return solve(m - 1, n - 1)