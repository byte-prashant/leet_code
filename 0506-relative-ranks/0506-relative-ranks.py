class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:

        import heapq
        ans = score[:]
        heap = [-val for val in score]
        heapq.heapify(heap)
        score_to_index = {val:index for index, val in enumerate(score)}
        count =1
        while heap:

            ele  = - heapq.heappop(heap)
            if count ==1:
                ans[score_to_index[ele]]  = "Gold Medal"

            if count ==2:
                ans[score_to_index[ele]]  = "Silver Medal"

            if count ==3:
                ans[score_to_index[ele]]  = "Bronze Medal"
            
            if count >=4:
                ans[score_to_index[ele]]  = str(count)

            count+=1

        return ans
            


