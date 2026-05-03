class Solution:
    def countSubstrings(self, s: str) -> int:
        ans =0
        def expand(i,j,s):
            count = 0
            while i>=0 and j<len(s) and s[i]==s[j]:
                count+=1
                i-=1
                j+=1
            return count
            
        for i in range(len(s)):
            ans+=expand(i,i,s)
            ans+=expand(i,i+1,s)
        return ans

      

