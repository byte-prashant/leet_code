class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        for a in range(len(nums)-3):
            if a>0 and nums[a-1] == nums[a]:
                continue

            for b in range(a+1, len(nums)-2):
                if b>a+1 and nums[b-1] == nums[b]:
                    continue

                low = b+1
                high = len(nums)-1
                while low <high:
                    summ = nums[a]+nums[b]+nums[low]+nums[high]

                    if summ<target:
                        low+=1
                    elif summ>target:
                        high-=1
                    elif summ == target:
                        ans.append((nums[a],nums[b],nums[low],nums[high]))
                        low+=1
                        high-=1
                        
                        while low<high and nums[low-1] == nums[low]:
                            low+=1
                        while low<high and nums[high] == nums[high+1]:
                            high-=1

                        
        return ans

            
        