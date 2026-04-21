class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        directions = [(0,1),(0,-1),(-1,0),(1,0)]

        queue = []
        for x in range(len(board)):
            for y in range(len(board[0])):
                if x==0 or x==len(board)-1 or y ==0 or y == len(board[0])-1:
                    if board[x][y] == "O":
                        queue.append((x,y))

        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] == "O":
                    board[x][y] = -1

        print(board,queue)
        while queue:
            x,y = queue.pop(0)
            board[x][y] = "O"
            for dx,dy in directions:

                new_x,new_y = x+dx,y+dy

                if new_x>=0 and new_x<len(board) and new_y>=0 and new_y<len(board[0]):

                    if board[new_x][new_y] == -1:

                        board[new_x][new_y] = "O"

                        queue.append((new_x,new_y))
        print(board,queue)
        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] == -1 :
                    board[x][y] =  "X"


                

        