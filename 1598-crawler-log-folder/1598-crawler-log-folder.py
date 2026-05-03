class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = 0
        for com in logs:
            if com =="../":
                if count:
                    count-=1
            elif com=="./":
                pass
            else:
                count+=1

        return count
        