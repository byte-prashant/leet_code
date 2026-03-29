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



            
        