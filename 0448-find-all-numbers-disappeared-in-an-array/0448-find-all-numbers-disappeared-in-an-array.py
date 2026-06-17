class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        num_freq = Counter(nums)
        return [ i for i in range(1,len(nums)+1) if i not in num_freq]
        