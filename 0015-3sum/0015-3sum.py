class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        ans = {}
        ele = []
        def backtrack(pos):
            if len(ele) == 3:
                if sum(ele) == 0:
                    key = tuple(sorted(ele[:]))
                    if not key in ele:
                        ans[key] = 1
                return
            for i in range(pos, len(nums)):
                ele.append(nums[i])
                backtrack(i+1)
                ele.pop()
            return

        def three_sum():
            backtrack(0)
            output = []
            for key, val in ans.items():
                output.append(list(key))
            return output


# as in above method we have only one args, so it means state neads only one args
# two states differ by one argument

# 3 level of  states for an ans 
# means n3 time complexity for all triplets [i>j>k] where i,j,k < n


# other ways find two sum
        # output = []
        # def three_sum():
            
        #     for i in range(len(nums)):
        #         for j in range(i+1,len(nums)):
        #             ans[nums[i]+nums[j]] = [nums[i], nums[j]]

        #     for k in range(len(nums)):
        #         if  -nums[k] in ans:
        #             print(k, ans[-nums[k]][:])
        #             temp = ans[-nums[k]][:]
        #             temp.append(nums[k])
        #             output.append(temp)

        #     print(ans)
        #     return output

        def three_sum():
            res, dups = set(), set()
            seen = {}
            for i, val1 in enumerate(nums):
                if val1 not in dups:
                    dups.add(val1)
                    # resetting the hash so that we  avoid including the val2 from prev run
                    # we can also do it by seen[val2]==i, as following
                    seen={}
                    for j, val2 in enumerate(nums[i + 1 :]):
                        complement = -val1 - val2
                        if complement in seen :
                            res.add(tuple(sorted((val1, val2, complement))))
                        seen[val2] = i
                    #print(seen)
            return res


        def three_sum():
            res, dups = set(), set()
            seen = {}
            for i, val1 in enumerate(nums):
                if val1 not in dups:
                    dups.add(val1)
                    
                    for j, val2 in enumerate(nums[i + 1 :]):
                        complement = -val1 - val2
                        if complement in seen  and seen[complement]==i:
                            res.add(tuple(sorted((val1, val2, complement))))
                        seen[val2] = i
                    #print(seen)
            return res
        return three_sum()




 


        