class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        matrix = [[0 for _ in range(rows)] for _ in range(cols)]
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        total = rows*cols

        def is_within_boundary(x,y):

            return x >=0  and x< len(matrix) and y>=0 and y<len(matrix[0])

        def make_turn(x,y,direction):
            next_dir = (direction+1)%4
            if  matrix[x+directions[next_dir][0]][y+directions[next_dir][1]]==0:
                return matrix[x+directions[next_dir][0]][y+directions[next_dir][1]]==0, next_dir
            else:
                return matrix[x+directions[next_dir][0]][y+directions[next_dir][1]]==0, direction

       

        x,y = rStart,cStart
        direction = 0
        ans = []
        while True and total>0:

            matrix[x][y]= 1
            total-=1
            ans.append([x,y])
            if total ==0:
                break
            new_x,new_y = x+directions[direction][0],y+directions[direction][1]
            if is_within_boundary(new_x,new_y):
                is_turned, new_direction = make_turn(new_x,new_y,direction)
                x,y,direction = new_x+directions[direction][0],new_y+directions[direction][1],new_direction
            else:
                _x,_y = x,y
                new_direction = (direction+1)%4
                while matrix[_x][_y]!=1:
                    if not is_within_boundary(new_x,new_y):
                        new_direction = (new_direction+1)%4
                        _x,_y =  _x+directions[_direction][0],_y+directions[new_direction][1]
                    else:
                        _x,_y =  _x+directions[_direction][0],_y+directions[new_direction][1]

                x,y,direction = _x,_y,new_direction

        
        return ans

    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        total = rows*cols
        steps = 1
        ans = []
        direction  = 0
        x,y = rStart,cStart
        while total>0:

            for _ in range(2):
                for _ in range(steps):
                    if total>0  :
                        dx,dy = directions[direction]
                        if x>=0 and x<rows and y>=0 and y<cols:
                            ans.append((x,y))
                            total-=1
                        x,y = x+dx,y+dy
                    else:
                        break

                direction = (direction+1)%4
            steps+=1
        
        return ans
















          














        