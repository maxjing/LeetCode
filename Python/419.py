class Solution:
    def countBattleships(self, board):
        m=len(board)
        n=len(board[0])
        res=0
        for i in range(m):
            for j in range(n):
                if board[i][j]==".":
                    continue
                if i>0 and board[i-1][j]=="X":
                    continue
                if j>0 and board[i][j-1]=="X":
                    continue
                res+=1
        return res

'''
only add new ship, how to check if it is part of existing ship?
1. check above [i-1][j] has x or not
2. check left [i][j-1] has x or not

'''