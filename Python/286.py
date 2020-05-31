class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        self.dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        if not rooms:
            return []
        for r in range(len(rooms)):
            for c in range(len(rooms[0])):
                if rooms[r][c] == 0:
                    self.dfs(rooms, r, c, 0)

    def dfs(self, rooms, r, c, d):
        for x, y in self.dirs:
            # 2020.05.30 only write the smallest d, that's why > room[r][c]
            if 0 <= r+x < len(rooms) and 0 <= c+y < len(rooms[0]) and rooms[r+x][c+y] > rooms[r][c]:
                rooms[r+x][c+y] = d + 1
                self.dfs(rooms, r+x, c+y, d+1)


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        m = len(rooms)
        if m == 0:
            return
        n = len(rooms[0])
        q = deque()
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.append((i, j))
        while q:
            row, col = q.popleft()
            for dx, dy in dirs:
                r, c = row + dx, col + dy
                if r < 0 or c < 0 or r >= m or c >= n or rooms[r][c] != 2 ** 31 - 1:
                    continue
                rooms[r][c] = rooms[row][col] + 1
                q.append((r, c))
