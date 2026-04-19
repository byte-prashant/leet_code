class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        parent = [ i for i in range(n)]
        size = [0]*n

        def find(node):
            if parent[node]!=node:
                parent[node] = find(parent[node])

            return parent[node]

        def union(node1,node2):
            parent1 = find(node1)
            parent2 = find(node2)    

            if parent1!=parent2:
                parent[parent1] = parent2

        
        for edge in edges:
            union(edge[0],edge[1])
      
        return find(source)==find(destination)

           