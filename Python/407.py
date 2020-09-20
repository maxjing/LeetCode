class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n = len(heightMap), len(heightMap[0])
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        heap = []
        visited = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                    heappush(heap, (heightMap[i][j], i, j))
                    visited[i][j] = 1
        res = 0
        while heap:
            height, x, y = heappop(heap)
            for dx, dy in dirs:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < m and 0 <= new_y < n and visited[new_x][new_y] != 1:
                    res += max(0, height - heightMap[new_x][new_y])
                    heappush(heap, (max(height, heightMap[new_x][new_y]), new_x, new_y))
                    visited[new_x][new_y] = 1
        return res
