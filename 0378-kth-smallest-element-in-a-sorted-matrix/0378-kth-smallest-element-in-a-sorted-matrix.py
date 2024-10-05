class Solution:
    import heapq
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        heap  = []
        for c in range(min(k,len(matrix[0]))):
            heap.append((matrix[0][c],[0,c]))
        heapq.heapify(heap)

        kth_ele = None
        while(k>0):

        
            kth_ele = heapq.heappop(heap)
            prev_row, prev_col = kth_ele[1]
            if prev_row< len(matrix)-1:
                heapq.heappush(heap,(matrix[prev_row+1][prev_col],[prev_row+1,prev_col]))

            k-=1
            


        return kth_ele[0]





        