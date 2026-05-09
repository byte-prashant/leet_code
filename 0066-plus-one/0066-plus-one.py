class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        integer = "".join(map(str, digits))
        integer = str(int(integer)+1)

        return [int(s) for s in integer] 