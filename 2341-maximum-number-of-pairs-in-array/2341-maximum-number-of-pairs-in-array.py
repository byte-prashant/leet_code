class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        from collections import Counter
        freq_data = Counter(nums)
        freq_map = [[]for _ in range(len(nums)+1)]
        for node, freq in freq_data.items():
            freq_map[freq].append(node)
        rem = 0
        for index , elems in enumerate(freq_map):
            if index>0 and index & 1:
                rem+=len(elems)
        
        return [int((len(nums)-rem)/2),rem]
        