class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        if m <= 1:
            return matrix
        for i in range(m):
            for j in range(i, m):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j],
        for i in range(m):
            matrix[i].reverse()

'''
1. switch m[i][j] with m[j][i]
123       147
456   ->  258
789       369
2. reverse each row
'''