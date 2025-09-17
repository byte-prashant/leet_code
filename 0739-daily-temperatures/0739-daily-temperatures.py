class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        ans = [0]*len(temperatures)
        if len(temperatures)==1:
            return [0]
        stack = [len(temperatures)-1]
        ans[-1] = 0
        
        for index in range(len(temperatures)-2,-1,-1):
            while stack and temperatures[stack[-1]]<=temperatures[index]:
                stack.pop()
            
            
            ans[index]= stack[-1] - index if stack else 0
            stack.append(index)

        return ans



            


        