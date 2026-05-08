class Solution:
    def removeStones(self, stones):
        
        maxRow = max(r for r, c in stones)
        maxCol = max(c for r, c in stones)
        
        OFFSET = maxRow + 1
        n = maxRow + maxCol + 2   # total DSU size
        
        parent = [i for i in range(n)]
        size = [1] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return
            
            if size[px] >= size[py]:
                parent[py] = px
                size[px] += size[py]
            else:
                parent[px] = py
                size[py] += size[px]

        # union row and column
        for r, c in stones:
            union(r, c + OFFSET)

        # count unique components
        roots = set()
        for r, c in stones:
            roots.add(find(r))

        return len(stones) - len(roots)