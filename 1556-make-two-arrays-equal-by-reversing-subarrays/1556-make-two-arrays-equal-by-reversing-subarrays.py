class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:

        target = Counter(target)
        for num in arr:
            if not num in target or target[num]==0:
                return False

            target[num] -=1
            

        return True

        