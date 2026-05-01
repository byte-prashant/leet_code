class Solution:
    def minimumSteps(self, s: str) -> int:
        right  =len(s)-1
        left = right
        while right>=0:
            if not s[right] =="0":  
                right-=1
            else:
                break

        if right==0:
            return 0
        print(right)
        left=right-1
        count = 0
        while left>=0 :

            if s[left]=="1":
                count+=right-left
              
                right-=1
            left-=1

        return count




        