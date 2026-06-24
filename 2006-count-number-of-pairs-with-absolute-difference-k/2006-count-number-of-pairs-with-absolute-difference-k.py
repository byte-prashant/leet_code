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
        
    def countKDifference(self, nums: List[int], k: int) -> int:
        seen = defaultdict(int)
        counter = 0
        for num in nums:
            tmp, tmp2 = num - k, num + k
            if tmp in seen:
                counter += seen[tmp]
            if tmp2 in seen:
                counter += seen[tmp2]
            
            seen[num] += 1
        
        return counter 