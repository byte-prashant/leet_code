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

    def countSubstrings(self, s: str) -> int:

        def expand(i,j,s):
            count = 0
            while i>=0 and j<len(s) and s[i] == s[j]:
                count+=1
                i-=1
                j+=1
            return count
        ans=0
        for i in range(len(s)):
            ans+=expand(i,i,s)
            ans+=expand(i,i+1,s)
        return ans


class Solution:
    def countSubstrings(self, s: str) -> int:




        def expand(left, right):
            count =0
            while left>=0 and right<len(s) and s[left]==s[right]:

                left-=1
                right+=1
                count+=1

            return count

        ans = 0
        for pos in range(len(s)):
            ans+=expand(pos,pos)
            ans+=expand(pos,pos+1)

        return ans


            



      

