class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        dp  ={}
        def  dfs(row, index):
            if (row,index) in dp:
                return dp[(row,index)]

            
            if row >= len(triangle):
                return float("+inf")
            if index>= len(triangle[row]) or index<0:
                return float("+inf")

            if row == len(triangle)-1:
                return triangle[row][index]

            
            val = min(dfs(row+1,index),dfs(row+1,index+1))


            dp[(row,index)] = val+triangle[row][index]

            return dp[(row,index)]

        return dfs(0, 0)

            

            
