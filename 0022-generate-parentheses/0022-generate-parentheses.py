class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        

        ans = []
        def sol(s,count):

            if len(s)== 2*n :
                if  count ==0:
                    ans.append(s)
                return

            if len(s)>2*n:
                return


            if count>0:
                sol(s+"(",count+1)
                sol(s+")",count-1)
            
            if count ==0:
                sol(s+"(",count+1)


            return

        sol("",0)

        return ans




        