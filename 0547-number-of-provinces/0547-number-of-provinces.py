class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
 


        def find_province(node,visit):
            visit[node] = True
            for col in range(len(isConnected)):
                if isConnected[node][col] and not visit[col]:
                    find_province(col,visit)

            


        provinces =0 
        visit =[False]*len(isConnected)
        for row in range(len(isConnected)):
                if not visit[row]:
                
                    provinces+=1
                    find_province(row,visit)

        return provinces

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parent = [city for city in range(n)]
        size = [1 for _  in range(n)]

        def find_parent(node):
            if parent[node]!=node:
                parent[node] = find_parent(parent[node])

            return parent[node]

        def union(node1,node2):

            p1 = find_parent(node1)
            p2 = find_parent(node2)

            if p1!=p2:
                if size[p1]>size[p2]:
                    parent[p2] = p1
                    size[p1]+=size[p2]
                    size[p2] =0

                else:
                    parent[p1] = p2
                    size[p2]+=size[p1]
                    size[p1] =0

        
        for row in range(len(isConnected)):
            for col in range(len(isConnected[0])):
                if isConnected[row][col] ==1:
                    union(row,col)


        count =0 

        for s in size:
            if s>0:
                count+=1

        return count






            
        