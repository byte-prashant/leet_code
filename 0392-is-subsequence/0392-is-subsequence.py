class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if len(s)>len(t):
            return False
        count = 0
        for ch in t:
            if count+1<=len(s) and ch == s[count] :
                count+=1
      
        if count == len(s):
            return True
        return False


        