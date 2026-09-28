class Solution:
    def numDecodings(self, s: str) -> int:

        string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        dp = {str(index+1):val for index, val in enumerate(string)}

        state = {}
        ans = [0]
        def sol(pos):


            if pos>=len(s):
                ans[0]+=1
                return

            path1 = s[pos]

            if path1 in dp:
                sol(pos+1)

            if len(s)-1>=pos+1:
                path2 = path1+s[pos+1]

                if path2 in dp:
                    sol(pos+2)

            return
        sol(0)

        return ans[0]



class Solution:
    def numDecodings(self, s: str) -> int:

        string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        dp = {str(index+1):val for index, val in enumerate(string)}

        state = {}
        ans = [0]
        def sol(pos):


            if pos in state:
                return state[pos]

            if pos>=len(s):
                
                return 1

            path1 = s[pos]

            ans = 0
            if path1 in dp:
                ans+=sol(pos+1)

            if len(s)-1>=pos+1:
                path2 = path1+s[pos+1]

                if path2 in dp:
                    ans+=sol(pos+2)

            state[pos] = ans

            return  state[pos]

        return sol(0)


        


        