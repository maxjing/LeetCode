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
                    # -2 is the maximum it can reach when x = 0

                    if newX < -2 or newY < -2 or (newX, newY) in visited:
                        continue
                    visited.add((newX, newY))
                    q.append((newX, newY))
        return step


class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        if x == 0 and y == 0:
            return 0
        dirs = [(1, 2), (-1, 2), (1, -2), (2, 1), (2, -1), (-2, 1), (-1, -2), (-2, -1)]
        x, y = abs(x), abs(y)

        q = deque([(0, 0)])
        step = 0
        visited = set()
        while q:
            step += 1
            size = len(q)
            for _ in range(size):
                m, n = q.popleft()
                for dx, dy in dirs:
                    newx, newy = m + dx, n + dy
                    if newx == x and newy == y:
                        return step
                    # 这里可以是 < -1
                    # For example, to reach (1,1) from (0, 0), the best way is to get (2, -1) or (-1, 2) first, then (1,1) (two steps). If we eliminate all coordinates with negative numbers, then we can't reach (1,1) from (0, 0) within two steps.
                    # 因为限制了 abs(x), abs(y) newx, newy 中必定是有一个是positive
                    if newx < -2 or newy < -2 or (newx, newy) in visited:
                        continue
                    else:
                        visited.add((newx, newy))
                        q.append((newx, newy))
        return step
