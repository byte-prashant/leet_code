class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:

        ans = {}
        arr = []
        dp = {}
        def combination(pos, addition):
            
            if len(arr) ==3 and addition<target:

                ans[tuple(arr[:])]=1
                
                return

            if len(arr)>3:
                return

            for index  in range(pos, len(nums)):
                arr.append(index)
                combination(index+1,addition+nums[index])
                arr.pop(-1)

            return

        combination(0,0)
        
        return len(ans)

    def threeSumSmaller(self, nums: List[int], target: int) -> int:

        elements = nums[:]
        elements = sorted(elements)
        ans = 0 
        print(elements)
        for index1 in range(len(nums)-2):
            val1 = elements[index1]
            left  = index1+1
            right = len(nums)-1
            while(left<right):
            
                summ = val1+elements[left]+elements[right]
                
                if summ<target:
                    #print(right,left)
                    ans+= right-left
                    left+=1
                else:
                    
                    right-=1

        return ans

    



        
                



        