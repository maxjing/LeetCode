class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        m, n = len(grid), len(grid[0])
        i, j = 0, 0
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count = self.dfs(grid, i, j)
                    res = max(count, res)
        return res

    def dfs(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
            return 0
        grid[i][j] = 0
        count = 0
        for dx, dy in self.dirs:
            count += self.dfs(grid, i + dx, j + dy)
        return count + 1