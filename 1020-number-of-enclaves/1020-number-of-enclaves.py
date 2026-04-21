class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        from collections import deque

        queue = deque()
        directions = [(-1,0),(1,0),(0,1),(0,-1)]

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if x==0 or y ==0 or x == len(grid)-1 or y ==len(grid[0])-1:

                    if grid[x][y] ==1:
                        queue.append((x,y))
                        grid[x][y] =0

        


        while queue:

            x,y = queue.popleft()
           
            for dx,dy in directions:
                new_x,new_y = x+dx,y+dy

                if new_x>=0 and new_x<len(grid) and new_y>=0 and new_y<len(grid[0]):

                    if grid[new_x][new_y] ==1:
                        grid[new_x][new_y]  = 0

                        queue.append((new_x,new_y))

    

        count = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    count+=1

        return count

       



        