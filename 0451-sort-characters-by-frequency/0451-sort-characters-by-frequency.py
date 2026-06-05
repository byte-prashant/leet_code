class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter
        frequencies = Counter(s)
        freq = [(ele, fre) for ele ,fre in frequencies.items()]
        freq.sort(key = lambda x : -x[1])
        ans = ""
        for key, f in freq:
            ans+= key*f
        return ans




        