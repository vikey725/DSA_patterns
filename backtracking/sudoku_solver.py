import math

def solve_sudoku(board):
    # tracker
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    blocks = [set() for _ in range(9)]
    solved = False

    # replicate current board
    for r in range(9):
        for c in range(9):
            if board[r][c] != ".":
                num = int(board[r][c])
                rows[r].add(num)
                cols[c].add(num)

                block_id = (r // 3) * 3 + (c // 3)
                blocks[block_id].add(num)

    def solve(r, c):
        nonlocal solved
        if r == 9:
            solved = True
            return

        nr = r + (c + 1) // 9
        nc = (c + 1) % 9
        block_id = (r // 3) * 3 + (c // 3)

        if board[r][c] != ".":
            solve(nr, nc)
        else:
            for num in range(1, 10):
                if num not in rows[r] and num not in cols[c] and num not in blocks[block_id]:
                    rows[r].add(num)
                    cols[c].add(num)
                    blocks[block_id].add(num)
                    board[r][c] = str(num)

                    solve(nr, nc)

                    if not solved:
                        rows[r].remove(num)
                        cols[c].remove(num)
                        blocks[block_id].remove(num)
                        board[r][c] = "."
        return solved
    
    solve(0, 0)







