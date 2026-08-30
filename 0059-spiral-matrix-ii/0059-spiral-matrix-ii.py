class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        matrix = matrix[:]
        
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        pos_x,pos_y = 0,0
        direction  = 0
        ans = []
        value  = 0
        while True:
            value+=1
            change = 0
            
          
            matrix[pos_x][pos_y] = value
          

            new_pos_x = pos_x+directions[direction][0]
            new_pos_y = pos_y +directions[direction][1]
            #change =1
            while change <=2:
                if  (new_pos_x>=0 and new_pos_x<len(matrix) and new_pos_y>=0 and new_pos_y< len(matrix[0]) and  matrix[new_pos_x][new_pos_y]!=0 ) or  not (new_pos_x>=0 and new_pos_x<len(matrix) and new_pos_y>=0 and new_pos_y< len(matrix[0])):
                    direction = (direction+1)%4
                    new_pos_x = pos_x+directions[direction][0]
                    new_pos_y = pos_y +directions[direction][1]
                    change+=1
                else:
                    break

            if change >=2:
                break

            pos_x,pos_y = new_pos_x,new_pos_y


        return matrix




class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        pos = (0,0)
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        matrix = [[0 for _ in range(n)] for j in range(n)]

        change = 0
        new_dir = 0
        num = 1
        new_row, new_col = pos[0],pos[1]
        while change<=1:


            row,col = new_row,new_col
            if row<n and row>=0 and col>=0 and col<n and  matrix[row][col]==0:
                matrix[row][col] = num
                change = 0
                num+=1

            else:
                new_dir =(new_dir+1)%len(directions)
                new_direction = new_dir
                change+=1
                # IMPORTANT:
                # Go back to the previous valid position
                row -= directions[(new_dir - 1) % 4][0]
                col -= directions[(new_dir - 1) % 4][1]


            dx,dy = directions[new_dir][0],directions[new_dir][1]
            new_row, new_col = row+dx,col+dy
            print(new_row, new_col )

        return matrix
