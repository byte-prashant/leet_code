class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        comb = {")":"(","}":"{","]":"["}
        for ch in s:
            
            if stack :
                
                if ch in comb:
                    if stack[-1]  == comb[ch]:
                        stack.pop(-1)
                        continue

                
            stack.append(ch)
            
          

        return False if stack else True
        