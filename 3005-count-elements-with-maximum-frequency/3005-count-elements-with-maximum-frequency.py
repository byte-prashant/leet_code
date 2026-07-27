class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:

        freq = Counter(nums)
       
        max_freq = 0
        for key, val in freq.items():
            max_freq = max(max_freq,val)
        
        
        count = 0
        for key, val in freq.items():
            if val == max_freq:
                count+=1
        return count*max_freq

        

            