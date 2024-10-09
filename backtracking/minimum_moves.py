def minimum_moves(grid):
    min_moves = float('inf')
    total = sum(sum(row) for row in grid)

    if total != 9:
        return -1

    zeros = [(i, j) for i in range(3) for j in range(3) if grid[i][j] == 0]
    extras = [[i, j, grid[i][j] - 1] for i in range(3) for j in range(3) if grid[i][j] > 1]

    if len(zeros) == 0:
        return 0

    def solve(i, count):
        if i >= len(zeros):
            nonlocal min_moves
            min_moves = min(min_moves, count)
            return
        
        for j in range(len(extras)):
            if extras[j][2] != 0:
                extras[j][2] -= 1
                solve(i + 1, abs(extras[j][0] - zeros[i][0]) + abs(extras[j][1] - zeros[i][1]) + count)
                extras[j][2] += 1

    solve(0, 0)
    return min_moves