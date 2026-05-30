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




