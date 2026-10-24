class Solution:
    def countHomogenous(self, s: str) -> int:

        last_occ = 0
        ans =0
        for index in range(len(s)):

            if s[index] == s[last_occ]:
                continue

            n = index-last_occ
           
            ans+=int((n*(n+1))/2)
            last_occ = index
        
        n = len(s)-last_occ
        
        ans+=int((n*(n+1))/2)
        last_occ = index

        



        return ans%(10**9+7)  
        