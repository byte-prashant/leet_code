class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        ans = []

        def sol(start, perm):
            if start == len(nums)-1:
                ans.append(perm[:])
                return

            for  beg in range(start, len(nums)):

                nums[beg],nums[ start] = nums[start], nums[beg]

                sol(start+1 , nums)

                nums[beg], nums[ start] = nums[start], nums[beg]

            return

        sol(0, nums)
        return ans 


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        ans = []
        def sol(combo):

            if len(combo) == len(nums):
                ans.append(combo[:])

                return

            for num in nums:
                if not num in combo:

                    combo.append(num)
                    sol(combo)
                    combo.pop()

            return
        sol([])
        return ans



        