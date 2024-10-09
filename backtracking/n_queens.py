def solve_n_queens(n):
    visited_cols = set()
    visited_pos_diagonals = set()
    visited_neg_diagonals = set()

    res = []
    board = [["."] * n for row in range(n)] # -> [['.', '.', '.', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.']]
    count = 0

    def backtrack(r):
        nonlocal count
        if r == n:
            count += 1
            copy = ["".join(row) for row in board]
            res.append(copy)
            return
        
        for c in range(n):
            if c in visited_cols or (r + c) in visited_pos_diagonals or (r - c) in visited_neg_diagonals:
                continue

            visited_cols.add(c)
            visited_pos_diagonals.add(r + c)
            visited_neg_diagonals.add(r - c)
            board[r][c] = "Q"

            backtrack(r + 1)

            visited_cols.remove(c)
            visited_pos_diagonals.remove(r + c)
            visited_neg_diagonals.remove(r - c)
            board[r][c] = "."

    backtrack(0)

    return res, count 

res, count = solve_n_queens(4)

print(res)
print(count)


