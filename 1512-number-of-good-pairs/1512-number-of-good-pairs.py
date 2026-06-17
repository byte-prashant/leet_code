class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        pairs = [(val,pos) for pos,val in enumerate(nums)]
        pairs.sort()
        count = 0
        prev =None
        local_count = 0
        for pos in range(len(pairs)-1,-1,-1):

            if prev:
                if pairs[prev][0] == pairs[pos][0]:
                    local_count+=1
                    count+=local_count
                else:
                    prev = pos
                    local_count=0
            else:
                prev = pos

        return count





        