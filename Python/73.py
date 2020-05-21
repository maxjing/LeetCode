class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        zeroRows = [False] * m
        zeroColumns = [False] * n
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zeroRows[i] = True
                    zeroColumns[j] = True
        for i, zeroed in enumerate(zeroRows):
            if zeroed:
                matrix[i] = [0] * n
        for i, zeroed in enumerate(zeroColumns):
            if zeroed:
                for r in range(m):
                    matrix[r][i] = 0



