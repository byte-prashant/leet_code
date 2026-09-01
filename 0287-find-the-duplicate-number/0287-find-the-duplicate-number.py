class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]
        while True:
            slow  = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        #return slow
        slow =  nums[0]
        while slow!=fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n= len(nums)
        right = 0
        while right < len(nums):
            if nums[right] == right+1:
                right+=1
                continue

            if nums[right] == nums[nums[right]-1]:
                return nums[right]
            target = nums[right]-1
            nums[right],nums[target] = nums[target], nums[right]

        

        