class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return 0
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    self.dfs(grid, i, j)

        return count

    def dfs(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '#'
        for dx, dy in self.dirs:
            r, c = i + dx, j + dy
            self.dfs(grid, r, c)
