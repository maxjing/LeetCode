class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        if x == y == 0:
            return 0
        dirs = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
        q = deque([(0, 0)])
        step = 0
        visited = set()
        x, y = abs(x), abs(y)
        while q:
            step += 1
            qSize = len(q)
            for _ in range(qSize):
                nextX, nextY = q.popleft()
                for dx, dy in dirs:
                    newX, newY = nextX + dx, nextY + dy
                    if (newX, newY) == (x, y):
                        return step
                    #-2 is the maximum it can reach when x = 0
                    if newX < -2 or newY < -2 or (newX, newY) in visited:
                        continue
                    visited.add((newX, newY))
                    q.append((newX, newY))
        return step