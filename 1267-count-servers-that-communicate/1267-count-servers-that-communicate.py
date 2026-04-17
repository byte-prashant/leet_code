class Solution:
    def countServers(self, grid: List[List[int]]) -> int:

        total_parents = len(grid[0])+len(grid)

        # stating indexs will reprsent rows ans end will represent cols
        parent = [ i for i in range(total_parents)]
        size = [0 for i in range(len(parent))]

        def get_row(row):
            return row

        def get_col_parent(col):
            return len(grid)+col


        def get_parent(node):
            if parent[node]!= node:
                parent[node] = get_parent(parent[node])

            return parent[node]

        def union(node1, node2):
            node1 = get_parent(node1)
            node2 = get_parent(node2)
            
            if node2!= node1:
               
                if size[node1]>size[node2]:
                    parent[node2] = node1
                    size[node1] += size[node2] if  size[node2]>0 else 1
                    size[node2] =0
                else:
                    parent[node1] = node2
                    size[node2] += size[node1] if  size[node1]>0 else 1
                    size[node1] =0


        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]:
                    new_col = get_col_parent(col)
                    union(row,new_col)
                    #print(size,parent)
        total_sever =0
        comu = 0

       # print(size,parent)
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]:
                    total_sever+=1
                    new_col = get_col_parent(col)
                    if size[row]==1 or size[new_col]==1:
                        comu+=1

        return total_sever-comu

            
            

        


        