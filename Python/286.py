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
