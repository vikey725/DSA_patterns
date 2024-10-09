def word_search(grid, word):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = set()
    n, m = len(grid), len(grid[0])

    def backtrack(r, c, i):
        if i == len(word):
            return True
        
        if r < 0 or r >= n or c < 0 or c >= m or (r, c) in visited or grid[r][c] != word[i]:
            return False

        visited.add((r, c))

        found = False
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            found = found or backtrack(nr, nc, i + 1)

        visited.remove((r, c))
        return found
    
    for r in range(n):
        for c in range(m):
            if backtrack(r, c, 0):
                return True
                
    return False