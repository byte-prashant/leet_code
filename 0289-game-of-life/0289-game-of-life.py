class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        new_board = copy.deepcopy(board)
        neighbours =[(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(1,1),(-1,1),(1,-1)]

        for row in range(len(new_board)):
            for col in range(len(new_board[0])):
                live_cells = 0
                for dx,dy in neighbours:
                    if row+dx>=0 and row+dx<len(board) and col+dy >=0 and col+dy <len(new_board[0]) and new_board[row+dx][col+dy] ==1:
                        live_cells+=1
                print(live_cells, row,col)
                if new_board[row][col] ==1:
                    if live_cells<2:
                        board[row][col] =0

                    if live_cells>3:
                        board[row][col] =0
                else:

                    if live_cells==3:
                        board[row][col] =1

        

