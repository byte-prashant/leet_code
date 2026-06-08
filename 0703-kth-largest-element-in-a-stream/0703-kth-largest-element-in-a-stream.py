import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.h_nums = [num for num in nums]
        self.k = k
        heapq.heapify(self.h_nums)
        for _ in range(len(nums)-k):
            heapq.heappop(self.h_nums)
        

    def add(self, val: int) -> int:
        
        
       
        if len(self.h_nums)< self.k or self.h_nums[0]<val:
            heapq.heappush(self.h_nums,val)
            if len(self.h_nums)>self.k:
                heapq.heappop(self.h_nums)

           
        
       
        
        return self.h_nums[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)