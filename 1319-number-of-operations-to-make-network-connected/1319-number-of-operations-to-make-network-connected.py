class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections)<n-1:
            return -1

        size = [1]*n
        parent = [i for i in range(n)]


        def find(node):
            if parent[node]!=node:
                parent[node] = find(parent[node])
            return parent[node]

        remaining =0
        components = n
        for nodes in connections:
            n1,n2 = nodes
            p1 = find(n1)
            p2 = find(n2)
            
            if p1!=p2:
                if size[p1]>size[p2]:
                    parent[p2] = p1
                    size[p1]+=size[p2]

                else:
                    parent[p1] = p2
                    size[p2]+=size[p1]
                components-=1
            else:
                remaining+=1

        return components-1



                



        


        