class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        self.dirs = [(1, 0), (0, 1), (-1, 0), (0, -1), (-1, -1), (1, 1), (1, -1), (-1, 1)]
        x, y = click[0], click[1]
        if board[x][y] == 'M':
            board[x][y] = 'X'
            return board
        self.dfs(board, x, y)
        return board

    def dfs(self, board, x, y):
        if board[x][y] != 'E':
            return
        mine = 0
        for dx, dy in self.dirs:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < len(board) and 0 <= new_y < len(board[0]) and board[new_x][new_y] == 'M':
                mine += 1
        if mine == 0:
            board[x][y] = 'B'
        else:
            board[x][y] = str(mine)
            return
        for dx, dy in self.dirs:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < len(board) and 0 <= new_y < len(board[0]):
                self.dfs(board, new_x, new_y)


