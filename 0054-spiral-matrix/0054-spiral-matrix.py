class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        def sol(matrix):
            directions = [(0,1),(1,0),(0,-1),(-1,0)]
            VISITED  = "#"
            cols = len(matrix[0])
            rows = len(matrix)
            change_direction = 0
            curr_direction = 0
            row = col = 0
            result = [matrix[0][0]]
            matrix[0][0] = VISITED
            def get_next_cell(row, col,direction):
                new_row = row + directions[direction][0]
                new_col = col + directions[direction][1]
                return new_row, new_col

            def is_valid(row, col):
                return row<rows and row>=0 and col>=0 and col<cols and not matrix[row][col]=="#"
            while change_direction<2:
                
                while True:
                    next_row ,next_col = get_next_cell(row,col,curr_direction)

                    if not is_valid(next_row, next_col):
                        break

                    change_direction =0
                    row,col = next_row ,next_col
                    result.append(matrix[row][col])
                    matrix[row][col] =VISITED
                
                curr_direction=(curr_direction+1)%4
                change_direction+=1

            return result

                
            

        def sol(matrix):
            directions = [(0,1),(1,0),(0,-1),(-1,0)]
            VISITED  = "#"
            cols = len(matrix[0])
            rows = len(matrix)
            result =[]
            def get_next_cell(row, col,direction):
                new_row = row + direction[0]
                new_col = col + direction[1]
                return new_row, new_col

            def is_valid(row, col):
                return row<rows and row>=0 and col>=0 and col<cols and not matrix[row][col]=="#"

            def recur(row, col,dire_pos,result):

                result.append(matrix[row][col])
                matrix[row][col] = VISITED
                new_row, new_col = get_next_cell(row, col,directions[dire_pos])
                change_pos = 0
                while not is_valid(new_row, new_col) and change_pos<2:
                    dire_pos = dire_pos+1
                    if dire_pos>3:
                        dire_pos = 0
                    change_pos+=1
                    new_row, new_col = get_next_cell(row, col,directions[dire_pos])
                if change_pos<2:
                    recur(new_row, new_col,dire_pos, result)

                return
            recur(0,0,0,result)
            return result


# find bruteforce approach using any pattern
# check repitetivenes
# find patterns in given input see if solutin can be redefined
# in above question we are changing direction (0,1), (1,0) ==>(0,-1),(-1,0). ,means flipping the things
# keep copy and writted down cell index and columns index , then you will understand following 
        def sol(matrix):

            row,col = 0,-1
            direction = 1
            cols = len(matrix[0])
            rows = len(matrix)
            result = []
            while True:
                for _ in range(cols):
                    col+= direction
                    result.append(matrix[row][col])
                rows-=1
                
                for _ in range(rows):
                    row=row+direction
                    result.append(matrix[row][col]) 

                cols-=1
                
                if cols*rows<=0:
                    break
                # fliping the direction
                direction*=-1 

            return result

        def sol(matrix):
            print("you are inside right matrix")
            directions = [(0,1),(1,0),(0,-1),(-1,0)]
            VISITED  = "#"
            cols = len(matrix[0])
            rows = len(matrix)
            change_direction = 0
            curr_direction = 0
            row = col = 0
            result = [matrix[0][0]]
            matrix[0][0] = VISITED
            def get_next_cell(row, col,direction):
                new_row = row + directions[direction][0]
                new_col = col + directions[direction][1]
                return new_row, new_col

            def is_valid(row, col):
                return row<rows and row>=0 and col>=0 and col<cols and not matrix[row][col]=="#"
            while change_direction<2:
                
                
                next_row , next_col = get_next_cell(row,col,curr_direction)

                if  is_valid(next_row, next_col):
                    

                    change_direction =0
                    row,col = next_row ,next_col
                    result.append(matrix[row][col])
                    matrix[row][col] =VISITED
                else:
                
                    curr_direction=(curr_direction+1)%4
                    change_direction+=1

            return result

                
        return sol(matrix)

    
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        pos_x,pos_y = 0,0
        direction  = 0
        ans = []
        while True:
          
            change = 0
            
            element = matrix[pos_x][pos_y]
            matrix[pos_x][pos_y] = "x"
            ans.append(element)

            new_pos_x = pos_x+directions[direction][0]
            new_pos_y = pos_y +directions[direction][1]
            #change =1
            while change <=2:
                if  (new_pos_x>=0 and new_pos_x<len(matrix) and new_pos_y>=0 and new_pos_y< len(matrix[0]) and  matrix[new_pos_x][new_pos_y]=="x" ) or  not (new_pos_x>=0 and new_pos_x<len(matrix) and new_pos_y>=0 and new_pos_y< len(matrix[0])):
                    direction = (direction+1)%4
                    new_pos_x = pos_x+directions[direction][0]
                    new_pos_y = pos_y +directions[direction][1]
                    change+=1
                else:
                    print("brooke",new_pos_x,new_pos_y,change)
                    break

            if change >=2:
                break

            pos_x,pos_y = new_pos_x,new_pos_y


        return ans









        





        