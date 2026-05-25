class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count = 0
        stack = ""
        for brack in s:
            if brack == "(":
                stack+="("
            else:
                if stack:
                    stack = stack[:len(stack)-1]
                else:
                    count+=1

        valid_c = len(stack) if stack else 0
        
        return count +valid_c
        