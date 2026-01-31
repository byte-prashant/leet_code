class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        direction = [(1,0),(-1,0),(0,-1),(0,1)]
       
       
        def is_valid(row,col,visited):
            if row>=0 and row<len(grid) and col>=0 and col<len(grid[0]) and grid[row][col]!=0 and not (row,col) in visited:
                return True

        def bfs(queue,fresh_orange):
            visited = {}
           
            #visited[(row,col)]=1
            minute = 0
            while queue:
                
                orange_rotten = False
                level_length = len(queue)
                for i in range(level_length):
                    row,col  = queue.pop(0)
                    for r,c in direction:
                        new_r,new_c = row+r,col+c
                        if is_valid(new_r,new_c,visited):
                           
                            if grid[new_r][new_c]== 1:
                                fresh_orange-=1
                                orange_rotten = True
                            visited[(new_r,new_c)]=1
                            queue.append((new_r,new_c))
                if orange_rotten:
                    minute+=1
                if not orange_rotten and fresh_orange>0:
                    return None
            if fresh_orange ==0:
                return minute
            else:
                return None

        def find_rotten_oranges(grid):
            pos = []
            fresh_orange = 0
            for row in range(len(grid)):
                for col in range(len(grid[0])):
                    if grid[row][col]==2:

                        pos.append((row,col))
                    if grid[row][col] ==1:
                        fresh_orange+=1
            return pos,fresh_orange


        all_minutes = []
        all_rotten_orages,fresh_orange = find_rotten_oranges(grid)
        for row, col in all_rotten_orages:
            queue = all_rotten_orages
            minutes = bfs(queue,fresh_orange)
            if minutes:
                all_minutes.append(minutes)
        if all_minutes:
           return min(all_minutes)
        elif fresh_orange:
            return -1
        else:
            return 0


        