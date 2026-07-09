class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        from typing import List
        board = [["." for _ in range(n)] for _ in range(n)]
        ans = []
        def isafe(row,col):
            c=col
            while c>=0:
                if board[row][c]=="Q":
                    return False
                c-=1
            r,c=row,col
            while r>=0 and c>=0:
                if board[r][c]=="Q":
                    return False 
                r-=1
                c-=1
            r,c=row,col
            while r<n and c>=0:
                if board[r][c]=="Q":
                    return False
                r+=1
                c-=1
            return True
        def solve(col):
            if col==n:
                temp=[]
                for row in board:
                    temp.append("".join(row))
                ans.append(temp)
                return
            
            for row in range(n):
                if isafe(row,col):
                    board[row][col]="Q"
                    solve(col+1)
                    board[row][col]="."
        solve(0)
        return ans