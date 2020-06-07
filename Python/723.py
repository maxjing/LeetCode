class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        m, n = len(board), len(board[0])
        todo = False

        # check each row if there are 3 to delete
        for r in range(m):
            for c in range(n - 2):
                if abs(board[r][c]) == abs(board[r][c + 1]) == abs(board[r][c + 2]) != 0:
                    board[r][c] = board[r][c + 1] = board[r][c + 2] = -abs(board[r][c])
                    todo = True
        # check each column if there are 3 to delete
        for r in range(m - 2):
            for c in range(n):
                if abs(board[r][c]) == abs(board[r + 1][c]) == abs(board[r + 2][c]) != 0:
                    board[r][c] = board[r + 1][c] = board[r + 2][c] = -abs(board[r][c])
                    todo = True
        # after delete drop any one with positive value, and remain set to 0 by column
        for c in range(n):
            wr = m - 1
            for r in reversed(range(m)):
                if board[r][c] > 0:
                    board[wr][c] = board[r][c]
                    wr -= 1
            for r in range(wr, -1, -1):
                board[r][c] = 0

        return self.candyCrush(board) if todo else board