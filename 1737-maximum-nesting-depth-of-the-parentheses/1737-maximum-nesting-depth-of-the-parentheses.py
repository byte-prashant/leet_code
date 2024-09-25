class Solution:
    def maxDepth(self, s: str) -> int:
        
        stack  = []
        i = 0
        max_depth = 0
        while(i<len(s)):
            print(i)
            char = s[i]
            if char == "(":
                if not stack:
                    #stack.append("(")
                    stack.append(1)
                else:
                    last_count =  stack[-1]
                    #stack.append("(")
                    stack.append(last_count+1)

            elif char == ")":
                max_depth = max(max_depth,stack[-1])
                #stack.pop()
                stack.pop()

            else:
                pass

            i=i+1

        return max_depth

# in abouve stack only represents previous max_depth, we can just used a variable 
    def maxDepth(self, s: str) -> int:
        
        stack  = 0
        i = 0
        max_depth = 0
        while(i<len(s)):
            print(i)
            char = s[i]
            if char == "(":
                if not stack:
                    stack+=1
                else:
                    last_count =  stack
                
                    stack+=1

            elif char == ")":
                max_depth = max(max_depth,stack)
                #stack.pop()
                stack-=1

            else:
                pass

            i=i+1

        return max_depth

    def maxDepth(self, s: str) -> int:
        
        stack  = 0
        i = 0
        max_depth = 0
        while(i<len(s)):
            print(i)
            char = s[i]
            if char == "(":
                stack+=1
            elif char == ")":
                max_depth = max(max_depth,stack)
                #stack.pop()
                stack-=1
            else:
                pass
            i=i+1

        return max_depth




        