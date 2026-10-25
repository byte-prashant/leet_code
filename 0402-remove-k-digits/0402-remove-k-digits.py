class Solution:
    def removeKdigits(self, num: str, k: int) -> str:

        stack = []

        if k==1 and len(num)==1:
            return "0"


        for val in num:

            while stack and k>0 and stack[-1]>val:
                stack.pop()
                k-=1

            stack.append(val)
        

        stack = stack[:-k] if k > 0 else stack

        # Remove leading zeros
        result = ''.join(stack).lstrip('0')
        
        # Handle edge case where result might be empty
        return result if result else '0'                