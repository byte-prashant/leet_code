class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        from collections import Counter
        frequency = Counter(nums)
        ans,ans_freq = -1,0
        for elem, freq in frequency.items():
            if not elem&1:
                if ans_freq<freq:
                    ans = elem
                    ans_freq = freq
                elif ans_freq == freq:
                    if ans>elem:
                        ans = elem
        return ans
                


        