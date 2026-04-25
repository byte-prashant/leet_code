class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        from collections import Counter
        frequencies = Counter(nums)
        frequencies = [(elem, freq) for elem ,freq in frequencies.items()]

        # using quick select
        frequencies.sort(key = lambda x: x[1])
        #print(frequencies)
        return [ ele[0] for  ele in frequencies[len(frequencies)-k:]]
        