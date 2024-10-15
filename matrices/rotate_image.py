def rotate_image(matrix):
    m, n = len(matrix), len(matrix[0])

    for i in range(m):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
    for i in range(m):
        matrix[i] = matrix[i][::-1]
      
    return matrix