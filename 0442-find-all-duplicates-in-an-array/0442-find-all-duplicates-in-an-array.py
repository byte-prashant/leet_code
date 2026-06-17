class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        ans = []

        return [key for key,val in freq.items() if val ==2]
        