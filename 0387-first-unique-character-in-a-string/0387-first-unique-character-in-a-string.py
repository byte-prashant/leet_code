class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        freq_data = Counter(s)
        for index, character in enumerate(s):
            if freq_data[character] == 1:
                return index

        return -1