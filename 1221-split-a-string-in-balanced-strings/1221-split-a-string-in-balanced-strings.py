class Solution:
    def balancedStringSplit(self, s: str) -> int:

        count = 1 if s[0]=="R" else -1
        ans =0
        for ch in s[1:]:
            if ch == "R":
                count+=1
            else:
                count-=1
            if not count:
                ans+=1
        return ans

        