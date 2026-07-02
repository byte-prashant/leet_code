class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        col_in_grid= len(grid[0])
        row_n = len(grid)
        parent_len = col_in_grid*row_n
        parents = [i for i in range(parent_len+1)]
        size = [0 for i in range(parent_len+1)]
        size = [0 for _ in range(parent_len)]

        
        def row_to_parent(row):
            return col+row

        def col_to_parent(col):
            return col
        def get_node_index(row,col):

            return row*col_in_grid + col


        def find_parent(node):
            if parents[node]!= node:
                parents[node] = find_parent(parents[node])

            return parents[node]


        def union(node1,node2):
            p1 = find_parent(node1)
            p2 = find_parent(node2)

            if p1!=p2:

                if size[p1]>size[p2]:
                    parents[p2] = p1
                    size[p1]+=size[p2]
                    size[p2] = 0

                else:
                    parents[p1] = p2
                    size[p2]+=size[p1]
                    size[p1] = 0

        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        for r in range(row_n):
            for c in range(col_in_grid):
                if grid[r][c] == "1":
                    size[get_node_index(r, c)] = 1
                    
        for col in range(len(grid[0])):
            for row in range(len(grid)):
                if grid[row][col] =="1":
                    for dirr in directions:
                        dx ,dy = dirr
                        x,y = row+dx, col+dy

                        if  x>=0 and x <len(grid) and y>=0 and y<len(grid[0]) and grid[x][y] =="1":
                            node1 = get_node_index(row,col)
                            node2 =get_node_index(x,y)
                            union(node1,node2)

        count = 0
        for node  in size:
            if node>0:
                count+=1
        print(size)
        return count
                    

            




    
        
        