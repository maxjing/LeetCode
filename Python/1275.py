class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        if len(moves) < 5:
            return "Pending"
        i = 0
        grid = [[0] * 3 for _ in range(3)]
        for x, y in moves:
            if i % 2 == 0:
                grid[x][y] = 1
            else:
                grid[x][y] = -1
            i += 1
        return self.win(grid, len(moves))

    def win(self, grid, n):
        rows = [0] * 3
        cols = [0] * 3
        diag = 0
        rev_diag = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                rows[i] += grid[i][j]
                cols[j] += grid[i][j]
                if i == j:
                    diag += grid[i][j]
                if i + j == 2:
                    rev_diag += grid[i][j]
        if any([3 in rows]) or any([3 in cols]) or diag == 3 or rev_diag == 3:
            return 'A'
        elif any([-3 in rows]) or any([-3 in cols]) or diag == -3 or rev_diag == -3:
            return 'B'
        else:
            return "Draw" if n == 9 else "Pending"






