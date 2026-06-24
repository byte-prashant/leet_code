class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:

        ans = []
        prev = None
        for index, num in enumerate(nums):

            if num ==key:
                for pos in range(index-k,index):
                    if pos>=0:
                        ans.append(pos)
                prev = index

            if isinstance(prev,int)  and index <=prev+k:
                ans.append(index)
            else:
                prev = None

        return list(set(ans))
        