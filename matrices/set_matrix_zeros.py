def set_matrix_zeros(mat):
    m, n = len(mat), len(mat[0])
    zeros = [(r, c) for c in range(n) for r in range(m) if mat[r][c] == 0]
    
    for r, c in zeros:
        for i in range(m):
            mat[i][c] = 0
        for j in range(n):
            mat[r][j] = 0

    return mat