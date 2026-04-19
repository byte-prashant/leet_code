from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        def next_positive(pos):
            pos += 1
            while pos < len(nums):
                if nums[pos] >= 0:
                    return pos
                pos += 1
            return None

        def next_negative(pos):
            pos += 1
            while pos < len(nums):
                if nums[pos] < 0:
                    return pos
                pos += 1
            return None

        curr_pos = 0
        pos = -1
        neg = -1
        positive = True
        ans = []
        while curr_pos < len(nums):
            if positive:
                pos = next_positive(pos)
                if pos is not None:
                    ans.append(nums[pos])
            else:
                neg = next_negative(neg)
                if neg is not None:
                    ans.append(nums[neg])
            curr_pos += 1
            positive = not positive

        return ans

            
                
        