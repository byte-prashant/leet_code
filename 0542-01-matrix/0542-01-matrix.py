class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        directions=[(1,0),(-1,0),(0,1),(0,-1)]

        def is_valid(x,y):

            return x>=0 and x<len(mat) and y>=0 and y < len(mat[0])

        queue = []
        rows, cols = len(mat), len(mat[0])

       
        visited =  visited = [[-1] * cols for _ in range(rows)]
        
        # Initialize queue with all 0s
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    queue.append((i, j, 0))
                    visited[i][j]  =0

        
        
        print(visited)

        while queue:
            new_queue = []
            pos_x,pos_y,dist = queue.pop(0)

            for dx,dy in directions:
                new_pos_x,new_pos_y,new_dis =  pos_x+dx,pos_y+dy,dist+1
                if is_valid(new_pos_x,new_pos_y):
                    if  visited[new_pos_x][new_pos_y]== -1:
                        #mat[new_pos_x][new_pos] = new_dis
                        queue.append((new_pos_x,new_pos_y,new_dis))
                        visited[new_pos_x][new_pos_y] = new_dis

                        


          


        return visited
            
        