class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        dp = {}
        def sol1():
            def sol(pos,c,nums):
                if tuple([pos,c]) in dp:
                    return  dp[tuple([pos,c])] 
                if c ==3:
                    return True

                if pos == len(nums):
                    return False

                is_triplet = False
                for ind in range(pos,len(nums)):
                    if nums[ind]>nums[pos]:
                        is_triplet = is_triplet or sol(ind,c+1,nums)
                dp[tuple([pos,c])] = is_triplet
                return is_triplet

            is_triplet = False
            for ind in range(0,len(nums)):
                
                is_triplet = is_triplet or sol(ind,1,nums)

            return is_triplet
        
        def sol2(nums):
            left = 0
            left_min = nums[0]
            index =1
            right_max = nums[len(nums)-1]
            right = [right_max]*len(nums)
           
            for ind in range(len(nums)-2,-1,-1):
                if right_max<nums[ind]:
                    right[ind] = nums[ind] 
                    right_max = nums[ind]
                else:
                     right[ind] = right_max

                
            print(right,right_max)
            while(index<len(nums)):
                if left_min<nums[index] and right[index]>nums[index]:
                    return True
                if left_min >nums[index]:
                    left_min = nums[index] 
               
                index+=1

            return False

        return sol2(nums)


        