class Solution:
    def isHappy(self, n: int) -> bool:
        dp = {n:1}
      
        while n!="1":
            new_s= 0
            for ch in str(n):
                new_s+= int(ch)*int(ch)
            
            n = str(new_s)
            print(n)
            if n in dp:
                return False
            dp[n] = 1
        return True

            
        