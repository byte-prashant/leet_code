class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        def two_sum():
            number = {}
            for pos, val in enumerate(nums):
                number[val] = pos
            ans = []
            for pos, val in enumerate(nums):
                if target-val in number and number[target-val]!=pos:
                    ans=[pos,number[target-val]]


            return ans

        def two_sum1():
            hashmap = {}
            for i in range(len(nums)):
                complement = target - nums[i]
                if complement in hashmap:
                    return [i, hashmap[complement]]
                hashmap[nums[i]] = i


        def two_sum1():
            hash_map = { }

            for i in range(len(nums)):
                com = target - nums[i]
                if com in hash_map:
                    return [i, hash_map[com]]
                hash_map[nums[i]] =i

            
        return two_sum()


## idea to find ksumm

        # def two_sum(elems,target):
        #     print("you are here")
        #     ans = []
        #     hashmap = {}
        #     for pos, val in enumerate(elems):

        #         if target-val in hashmap:
        #             ans.append([val,target-val])
        #         hashmap[val] = pos

        #     return ans


        # def ksum(elems, target, k):
        #     if target < 0:
        #         return []

        #     if k ==2:
        #         return two_sum(elems,target)

        #     result_set = []
        #     for pos in range(len(elems)):
        #         ans = ksum(elems[pos+1:], target-elems[pos], k-1)
        #         for subset in ans:
        #             result_set.append(ans.append(elems[pos]))

        #     return result_set
        # nums.sort()
        # return ksum(nums, target, 2)
        