class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        prev_pos = None
        left = index =0 
        total_count = cons_one =0
        while(index<len(nums)):
            if nums[index] == 0:
                
                if prev_pos:
                    cons_one = index-prev_pos-1
                prev_pos = index
            cons_one+=1
            total_count = max(total_count, cons_one)
            index=1+index
       
           
        return cons_one

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i = 0
        k=1
        for j in range(len(nums)):
            k -= 1 - nums[j]
            if k < 0:
                k += 1 - nums[i]
                i += 1
        return j - i + 1

        


        