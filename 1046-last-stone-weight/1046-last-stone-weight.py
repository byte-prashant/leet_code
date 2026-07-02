class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        heap = [ - stone for stone in stones]
        heapq.heapify(heap)
        
        while heap and len(heap)>1:
            stone1, stone2 = heapq.heappop(heap), heapq.heappop(heap)

            if stone1==stone2:
                continue
            diff = abs(abs(stone1)-abs(stone2))

            heapq.heappush(heap,-diff)

        return abs(heap[0]) if heap else 0
            


        