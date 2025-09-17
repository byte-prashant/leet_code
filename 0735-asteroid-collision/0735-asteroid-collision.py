class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [asteroids[0]]
        for  ast in asteroids[1:]:
            if ast<0:
                while(stack  and stack[-1]>0):
                    ele = stack.pop() 
                    if ele == abs(ast): 
                        break
                    if ele> abs(ast):
                        stack.append(ele)
                        break
                else:
                    stack.append(ast)

            else:
                stack.append(ast)
                    
                    
                   
        return stack



                
                


            
        