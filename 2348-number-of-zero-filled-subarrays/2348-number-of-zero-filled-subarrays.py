class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:

        if len(nums) ==1:
            if nums[0] ==0:
                return 1
            return 0
        count = 0
        left = None
        sections = []
        for right in range(len(nums)):
            if left == None:
                if nums[right] ==0:
                    left = right
                    if right==len(nums)-1 and nums[right] ==0:
                        n = right-left+1

                        sections.append((left,right))
                        count+= n*((n+1)/2)
            else:
                if nums[right]!=0 or right==len(nums)-1:
                    n = right-left 
                    if right==len(nums)-1 and nums[right] ==0:
                        n = right-left+1

                    sections.append((left,right))
                    count+= n*((n+1)/2)
                    left = None

          
        print(sections)
        return int(count)
        