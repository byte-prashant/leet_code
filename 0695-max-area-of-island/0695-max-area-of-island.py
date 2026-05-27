class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        neighbours = [(-1,0),(1,0),(0,1),(0,-1)]
        def is_valid(pos):
            x,y = pos[0],pos[1]

            return x>=0 and x<len(grid) and y>=0 and y<len(grid[0]) and grid[x][y]==1

        def dfs(pos):
            count= 0
            for neigh in neighbours:
                new_x,new_y = pos[0]+neigh[0],pos[1]+neigh[1]
                if is_valid(( new_x,new_y)):
                    grid[ new_x][new_y]  = -1
                    count+=dfs(( new_x,new_y ))+1
            return count

        maxx = 0

        for  row in  range(len(grid)):
            for col in range(len(grid[0])):

                if grid[row][col]==1:
                    grid[row][col] = -1
                    maxx = max(dfs((row,col))+1,maxx)
                   
        
        return maxx





