class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 1:
            return [[1]]
        seen = [[False] * n for _ in range(n)]
        #2020.05.20 initial res like this
        res = [[0] * n for _ in range(n)]
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        r = c = di = 0
        for i in range(1, n * n + 1):
            res[r][c] = i
            seen[r][c] = True
            rr, cc = r + dr[di], c + dc[di]
            if 0 <= rr < n and 0 <= cc < n and not seen[rr][cc]:
                r, c = rr, cc
            else:
                di = (di + 1) % 4
                r, c = r + dr[di], c + dc[di]
        return res

