class Solution:
    def countSquares(self, matrix):
        m, n = len(matrix), len(matrix[0])
        dp = [[0]*(n+1) for _ in range(m+1)]
        sum = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] > 0:
                    dp[i+1][j+1] = min(dp[i][j],dp[i+1][j],dp[i][j+1])+1
                    sum +=dp[i+1][j+1]
        return sum

'''
Time O(MN)
Space O(1)
similar with 221
'''