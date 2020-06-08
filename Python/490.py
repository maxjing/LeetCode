class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        q = deque([start])
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        while q:
            x, y = q.popleft()
            maze[x][y] = 2
            if x == destination[0] and y == destination[1]:
                return True
            for dx, dy in dirs:
                new_x, new_y = x + dx, y + dy
                while 0 <= new_x < len(maze) and 0 <= new_y < len(maze[0]) and maze[new_x][new_y] != 1:
                    new_x += dx
                    new_y += dy
                new_x -= dx
                new_y -= dy
                if maze[new_x][new_y] == 0:
                    q.append((new_x, new_y))
        return False
