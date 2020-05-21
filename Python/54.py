class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        m, n = len(matrix), len(matrix[0])
        seen = [[False] * n for _ in matrix]
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        r = c = di = 0
        res = []
        for _ in range(m * n):
            res.append(matrix[r][c])
            seen[r][c] = True
            cr, cc = r + dr[di], c + dc[di]
            if 0 <= cr < m and 0 <= cc < n and not seen[cr][cc]:
                r, c = cr, cc
            else:
                di = (di + 1) % 4
                r, c = r + dr[di], c + dc[di]
        return res

'''
dr = [0, 1, 0, -1], 0 means row not change, 1 means row + 1
seen is used to prevent [1,2,3,6,9,8,7,4,1] not [1,2,3,6,9,8,7,4,5], 1 repeated
'''