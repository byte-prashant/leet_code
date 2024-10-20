
class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []
        

    def addNum(self, num: int) -> None:
        heappush(self.left, -num)
        heappush(self.right, -self.left[0])
        heappop(self.left)

        if len(self.left)<len(self.right):
            heappush(self.left, -self.right[0])
            heappop(self.right)



        

    def findMedian(self) -> float:
        if len(self.left)>len(self.right):
            return - self.left[0]

        else:

            return (-self.left[0]+self.right[0])/2
            
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()