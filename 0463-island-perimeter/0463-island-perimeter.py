class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        def is_valid(x,y):
            return x<len(grid) and x>=0 and y<len(grid[0]) and y>=0
        visited = {}
        def dfs(x,y):
            
            if (x, y) in visited:
                return 0
            if x<len(grid) and x>=0 and y<len(grid[0]) and y>=0:


                count = 0
                visited[(x,y)] =1
                if is_valid(x+1,y) and grid[x+1][y] == 0:
                    count+=1
                else:
                    count+=dfs(x+1,y)

                if is_valid(x-1,y) and grid[x-1][y] == 0:
                    count+=1
                else:
                    count+=dfs(x-1,y)

                if is_valid(x,y+1) and grid[x][y+1] == 0:
                    count+=1
                else:
                    count+=dfs(x,y+1)

                if is_valid(x,y-1) and grid[x][y-1] == 0:
                    count+=1
                else:
                    count+=dfs(x,y-1)

                return count
            return 1

        for x  in range(len(grid)):
            for y in range(len(grid[0])):

                if grid[x][y] ==1:
                    return dfs(x,y)


        