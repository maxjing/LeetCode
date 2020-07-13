class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:

        if not grid or not grid[0]:
            return 0

        seen = set()
        m, n = len(grid), len(grid[0])
        distinctIslands = defaultdict(int)

        def dfs(i, j, curri, currj, shape):
            seen.add((curri, currj))
            for r, c in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = curri + r, currj + c
                if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in seen and grid[ni][nj] == 1:
                    # seen.add((ni, nj))
                    shape.add((ni - i, nj - j))
                    dfs(i, j, ni, nj, shape)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in seen:
                    shape = set()
                    dfs(i, j, i, j, shape)
                    shape = tuple(shape)
                    distinctIslands[shape] = 1

        return len(distinctIslands)