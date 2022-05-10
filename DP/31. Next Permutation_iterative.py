class Solution:
    # @param A : list of integers
    # @return a list of integers
    def nextPermutation(self, A):
        def nextPermutationSol(nums):

            l = len(nums)
            if l > 1:
                prev = nums[l - 1]
                curr = l - 2
                while (curr > 1):
                    if nums[curr] > prev:
                        prev = nums[curr]
                        curr -= 1
                    else:
                        break

                pos1, pos2 = curr, curr + 1
                curr = curr + 1
                found = False if nums[pos2] < nums[pos1] else True
                while (curr < l):

                    if nums[pos2] > nums[curr] and nums[curr] > nums[pos1]:
                        pos2 = curr
                        found = True

                    curr += 1
                if not found:
                    nums.sort()
                    return nums
                nums[pos1], nums[pos2] = nums[pos2], nums[pos1]

                num = nums[pos1 + 1:]

                num.sort()

                return nums[:pos1 + 1] + num

            else:
                return nums

        return nextPermutationSol(A)

