class Solution:
    def maxBalancedShipments(self, weight: List[int]) -> int:
        result = previous = 0
        for i in weight:
            if previous and previous > i:result += 1;previous = 0
            else:previous = i
        return result