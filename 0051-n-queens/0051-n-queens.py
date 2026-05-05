class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        left_diagonal = [False] *(2*n-1)
        right_diagonal = [False] * (2*n-1)
        cols =  [False] *n
        rows = [False]*n
        ans = []
        def play_chess(row,board):
            if row==n:
                ans.append(board)
                return

            for j in range(n):
                if  left_diagonal[j-row+n-1] or right_diagonal[j+row] or cols[j]:
                    continue

                left_diagonal[j-row+n-1] = right_diagonal[j+row] = cols[j]  = 1
                row_ch = ["."*(j)+"Q"+"."*(n-j-1)]

               # board.append(row_ch)
                print(board)
                play_chess(row+1,board+row_ch)
                #board.pop(-1)
                left_diagonal[j-row+n-1] = right_diagonal[j+row] = cols[j]  = 0

            return
        play_chess(0,[])
        return ans




            
