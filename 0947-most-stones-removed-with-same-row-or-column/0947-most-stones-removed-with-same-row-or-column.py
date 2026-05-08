class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        maxRow = max([ value[0] for value in stones])
        maxCol = max([ value[1] for value in stones])
        OFFSET = maxCol+1
        n = maxRow + maxCol + 2   # total DSU size
        parents = [ node for node in range(n)]
        size = [1 for _ in range(n)]

        def get_parent_index(row):
            return maxRow+1 + row

        
        def find_parent(node):
           # print(node)
            if parents[node]!= node:
                parents[node] = find_parent(parents[node])

            return parents[node]

        
        for row ,col in stones:
           
                if  True:
                    #print(col, row ,get_parent_index(row))
                    
                    parent_1 = find_parent(row)
                    parent_2 = find_parent(get_parent_index(col))
                    

                    if parent_1 != parent_2:
                        if size[parent_1]>=size[parent_2]:

                            size[parent_1]+= size[parent_2]
                            parents[parent_2] = parent_1
                            size[parent_2]=0

                        else:
                            size[parent_2]+= size[parent_1]
                            parents[parent_1] = parent_2
                            size[parent_1] =0
                    # else:
                    #     size[parent_1]+=1
                    #     size[parent_2]+=1
                    # print(parents)
                    # print(size)

        # roots = set()
        # for r, c in stones:
        #     roots.add(find_parent(r))
                

        #print(parents)
        roots = set()
        for r, c in stones:
            roots.add(find_parent(c+maxRow+1))

        return len(stones) - len(roots)

        
class Solutioln:
    def removeStones(self, stones):
        
        maxRow = max(r for r, c in stones)
        maxCol = max(c for r, c in stones)
        
        OFFSET = maxRow + 1
        n = maxRow + maxCol + 2   # total DSU size
        
        parent = [i for i in range(n)]
        size = [0] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                size[px]+= 1
                size[py]+= 1
                return
            
            if size[px] >= size[py]:
                parent[py] = px
                size[px] += size[py]+1
                size[py]= 0
            else:
                parent[px] = py
                size[py] += size[px]+1
                size[px] = 0

        # union row and column
        for r, c in stones:
            union(r, c + OFFSET)

        # print(parent)
        # print(size)
        # count unique components
        roots = set()
        for r, c in stones:
            roots.add(find(r))

        return len(stones) - len(roots)

        