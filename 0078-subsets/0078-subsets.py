class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:


        ans= []

        def find_subs(i,subs):
            if i>len(nums)-1:
                ans.append(subs[::])
                return


            subs.append(nums[i])
            find_subs(i+1,subs)
            subs.pop()

            if not subs or subs[-1]!=nums[i]:
                find_subs(i+1,subs)
            return

        find_subs(0,[])
        return ans

            
