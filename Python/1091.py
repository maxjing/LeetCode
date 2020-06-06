class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        #2020.06.05 means not way to start or no way to end the path
        if grid[0][0] or grid[n - 1][n - 1]:
            return -1
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1), (-1, 1), (1, -1), (1, 1), (-1, -1)]
        q = deque([(0, 0, 1)])

        while q:
            x, y, d = q.popleft()
            if x == n - 1 and y == n - 1:
                return d
            for dx, dy in dirs:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < n and 0 <= new_y < n and not grid[new_x][new_y]:
                    grid[new_x][new_y] = 1
                    q.append((new_x, new_y, d + 1))
        return -1
