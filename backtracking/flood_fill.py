def flood_fill(grid, sr, sc, target):
    rows, cols = len(grid), len(grid[0])
    source = grid[sr][sc]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def solve(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or  grid[r][c] != source or grid[r][c] == target:
            return
        
        grid[r][c] = target

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            solve(nr, nc)

    solve(sr, sc)
    return grid


