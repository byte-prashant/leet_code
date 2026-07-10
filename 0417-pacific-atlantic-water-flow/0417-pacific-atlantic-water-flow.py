class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:


        pacific = []
        atlantic = []
        for i in range(len(heights[0])):
            pacific.append((0,i))
        
        for i in range(len(heights)):
            pacific.append((i,0))
        
        for i in range(len(heights[0])):
            atlantic.append((len(heights)-1,i))
        
        for i in range(len(heights)):
            atlantic.append((i,len(heights[0])-1))

        def is_valid(row,col):

            return row<len(heights) and row>= 0 and col<len(heights[0]) and col>=0

    
        
        atlantic_reach = atlantic[:]
        pacific_reach = pacific[:]

        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        
        def bfs(queue, is_atlantic):
            seen = {}
            while queue:
                row,col  = queue.pop(0)
                seen[(row,col)] = 1
            

                for dx,dy in directions:

                    new_row = row+dx
                    new_col = col+dy
                    if is_valid(new_row, new_col) and not (new_row,new_col) in seen and heights[new_row][new_col]>=heights[row][col]:
                        seen[(new_row,new_col)] = 1
                        queue.append((new_row, new_col))
            return set(seen) 
        
        pacific_reach =bfs(pacific_reach, False)
        atlantic_reach = bfs(atlantic_reach, True)
        return list(atlantic_reach.intersection(pacific_reach))
        










        