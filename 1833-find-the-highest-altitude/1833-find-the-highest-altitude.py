class Solution:
    def largestAltitude(self, gain: List[int]) -> int:

        h_alt =  0
        prev =0
        for g in gain:
            h_alt = max(h_alt, prev+g)
            prev =prev+g

        return h_alt

        