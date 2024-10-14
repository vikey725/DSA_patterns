from collections import deque

def update_matrix(mat):
    q = deque()

    m = len(mat)
    n = len(mat[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for r in range(m):
        for c in range(n):
            if mat[r][c] == 0:
                q.append((r, c))
            else:
                mat[r][c] = '#'
    
    while q:
        r, c = q.popleft()
        for dr, dc in directions:
            nr = r + dr
            nc = c + dc

            if nr < 0 or nr >= m or nc < 0 or nc >= n or mat[nr][nc] == 0:
                continue 
            if mat[nr][nc] == '#':
                mat[nr][nc] = mat[r][c] + 1
                q.append((nr, nc))

    return mat