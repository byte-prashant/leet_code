class Solution:
    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:


        stack = []
        pos = 0
        for val in pushed:
            
            pop = popped[pos]

            while stack and stack[-1] == pop:
                stack.pop()
                pos+=1
                pop = popped[pos]
                

            if val == pop:
                pos+=1
                continue

            stack.append(val)
        
        #pop = popped[pos]
        while stack and pos<len(popped) and  stack[-1] == popped[pos] :
            stack.pop()
            pos+=1
            

        return True if not stack  else False
                



        