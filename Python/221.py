class Solution:
    def maximalSquare(self, matrix):
        if matrix is None or len(matrix) < 1:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])

        #2020.5.21 +1 是增加一个边界
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]
        max_side = 0

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == '1':
                    #+1 是因为就算min里面都是0，本身也能成为1*1的cube
                    dp[r + 1][c + 1] = min(dp[r][c], dp[r + 1][c], dp[r][c + 1]) + 1
                    max_side = max(max_side, dp[r + 1][c + 1])

        return max_side * max_side

'''
https://leetcode.com/problems/maximal-square/discuss/600149/Python-Thinking-Process-Diagrams-DP-Approach
'''