class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        self.q = deque()
        i, j = self.first(A)
        self.dfs(A, i, j)
        return self.bfs(A)

    def first(self, A):
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j]:
                    return i, j

    def dfs(self, A, i, j):
        A[i][j] = -1
        self.q.append((i, j, 0))
        for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
            if 0 <= x < len(A) and 0 <= y < len(A[0]) and A[x][y] == 1:
                self.dfs(A, x, y)

    def bfs(self, A):
        while self.q:
            i, j, level = self.q.popleft()
            for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if 0 <= x < len(A) and 0 <= y < len(A[0]):
                    if A[x][y] == 1:
                        return level
                    elif not A[x][y]:
                        A[x][y] = -1
                        self.q.append((x, y, level + 1))

