class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        left = 1
        right = 1
        count  = 0
        for right in range(1, len(nums)):
            if nums[right]!=nums[right-1]:
                    count = 0
                    nums[left] = nums[right]
                    left+=1
            else:
                    count+=1
                    if count<=1:
                        nums[left] = nums[right]
                        left+=1
           
        return left

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last_seen_ele = nums[0]
        stale_pos = 0
        count= 1
        for k in range(1, len(nums)):
            print(last_seen_ele, nums[k], count)
            if nums[k] == last_seen_ele:
                count +=1
                if count <3:
                    stale_pos+=1
                    nums[stale_pos] = nums[k]
            else:
                stale_pos+=1
                nums[stale_pos] = nums[k]
                last_seen_ele = nums[k]
                count = 1

        return stale_pos+1 

        


        
        