#https://leetcode.com/__Sixth__/
class Solution:
    def isSafe(self,board,row:int,col:int):
        if "Q" in [board[row][col] for row in range(row)]:return False
        if "Q" in [board[row-i][j] for i , j in enumerate(range(col,-1,-1))]:return False
        if "Q" in [board[row-i][j] for i , j in enumerate(range(col,len(board),1))]:return False
        return True
    def Solve(self,board,row,n):
        if not n:
            print(board)
        if row >= len(board):
            return
        for i in range(len(board)):
            if self.isSafe(board,row,i):
                board[row][i] = "Q"
                self.Solve(board,row+1,n-1)
                board[row][i] = "."
    def solveNQueens(self, n: int):
        board = [["." for i in range(n)] for j in range(n)]
        self.Solve(board,0,n)
Solution().solveNQueens(4)
