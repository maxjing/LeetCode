class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        d = collections.defaultdict(list)
        row, column = len(matrix), len(matrix[0])
        for i in range(row):
            for j in range(column):
                d[i + j].append(matrix[i][j])
        res = []
        for i in range(row + column - 1):
            if i % 2 == 0:
                #res += d[i][::-1]
                res.extend(d[i][::-1])
            else:
                res.extend(d[i])
        return res
