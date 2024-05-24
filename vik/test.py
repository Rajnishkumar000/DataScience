from typing import List

def rotate_over_diagonals(matrix: List[List[int]], turns: int) -> List[List[int]]:
    n = len(matrix)
    for _ in range(turns):
        matrix2 = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i + j < n-1:
                    matrix2[i][j+1] = matrix[i][j]
                elif i + j > n-1:
                    matrix2[i-1][j] = matrix[i][j]
                else:
                    matrix2[i][j] = matrix[i][j]
        matrix = matrix2
    return matrix
mat=[[1,2,3],[4,5,6],[7,8,9]]
turns=1
output=rotate_over_diagonals(mat,turns)
print(output)