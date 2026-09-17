def transpose_matrix(matrix):
    n = len(matrix)
    
    result = [[0] * n for _ in range(n)]
    
    
    for i in range(n):
        for j in range(n):
            result[j][i] = matrix[i][j]
            
    return result
mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Original Matrix:")
for row in mat:
    print(row)

transposed = transpose_matrix(mat)

print("\nTransposed Matrix:")
for row in transposed:
    print(row)
