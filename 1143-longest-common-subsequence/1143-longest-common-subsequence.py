class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        ans = [0]
        def common(i,j,text1,text2, count):
            if i >= len(text1) or j>= len(text2):
                ans[0] = max(ans[0],count)
                return 
            
            if text1[i] == text2[j]:
                common(i+1,j+1,text1,text2,count+1)
            common(i+1,j,text1,text2,count)
            common(i,j+1,text1,text2,count)
        
        common(0,0,text1,text2, 0)

        return ans[0]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        ans = [0]
        dp={}
        def common(i,j,text1,text2):
            # variable which may refers toa state ate i,j, count
            # i,j will refer to state
            # we can create dp
            
            if i >= len(text1) or j>= len(text2):
             
                return 0
            
            if (i,j) in dp:
                return dp[(i,j)]
            
            if text1[i] == text2[j]:
                dp[(i,j)]= common(i+1,j+1,text1,text2)+1
            
            else:
               
                dp[(i,j)] = max(common(i+1,j,text1,text2),common(i,j+1,text1,text2))

            return dp[(i,j)]
        
        common(0,0,text1,text2)

        return    common(0,0,text1,text2)
            
    
   