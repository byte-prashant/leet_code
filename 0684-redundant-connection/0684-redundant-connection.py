class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        parents = [node for node in range(len(edges))]

        ans = None
        size = [1] * len(edges)
        def find(node):
            if parents[node]!=node:
                parents[node] =  find(parents[node])
            return parents[node]

        for n1,n2 in edges:

            p1 = find(n1-1)
            p2  = find(n2-1)

            #print(p1,p2,n1,n2)

            if p1!=p2:
                if size[p1] > size[p2]:
                    parents[p2]=p1
                    
                    size[p1]+=size[p2]

                else:
                     parents[p1]=p2
                     size[p2]+=size[p1]
            else:
                ans = [n1,n2]

            #print(parents)

        return ans


