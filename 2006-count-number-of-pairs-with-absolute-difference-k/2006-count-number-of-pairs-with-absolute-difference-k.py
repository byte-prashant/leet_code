class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 0
        hash_map = {}
        for num in nums:
            if num-k in hash_map:
                ans+=hash_map[num-k]
               
            if num in hash_map:
                hash_map[num]+=1
            else:
                hash_map[num] = 1

            print(num-k,num,hash_map)
        return ans
        