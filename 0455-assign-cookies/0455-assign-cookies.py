class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        child=0
        for pos, chocolate_height in enumerate(g):
            while s and  s[0]<chocolate_height:
                s.pop(0)
            if s  and s[0]>=chocolate_height:
                s.pop(0)
                child+=1
        return child
        