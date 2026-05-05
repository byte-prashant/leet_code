class Solution:
    def isPalindrome(self, x: int) -> bool:
        disgits = {}
        if x<0:
            return False

        while(x>=10):
            digit = x%10
            disgits[digit] = disgits.get(digit,0)+1
            x = x//10
            
        digit = x
        disgits[digit] = disgits.get(digit,0)+1
        print(disgits)
        odd = 0 
        for key, val in disgits.items():
            if val &1 :
                odd+=1
            if odd>1:
                return False

        return True



            

    def isPalindrome(self, x: int) -> bool:
            s = str(x)
            return s == s[::-1]