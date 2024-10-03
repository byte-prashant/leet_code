class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        def sol1(nums):
            ans = []
            nums.sort()
            
            def permute(start=0):
                
                if start == len(nums):
                    ans.append(nums[:])
                    return
                dp = set()
                for i in range(start, len(nums)):
                    if  nums[i] not in dp:
                        dp.add(nums[i])
                        nums[start], nums[i] = nums[i], nums[start]
                        permute(start+1)
                        nums[start], nums[i] = nums[i], nums[start]

               # return

            permute(0)
            return ans


        def sol2(nums):
            def backtrack(start):
                if start == len(nums):
                    ans.append(nums[:])
                    return
                # we will not explaore for same start point
                unique = set()
                for i in range(start, len(nums)):
                    if nums[i] not in unique:
                        unique.add(nums[i])
                        nums[start], nums[i] = nums[i], nums[start]
                        backtrack(start + 1)
                        nums[start], nums[i] = nums[i], nums[start]
            
            ans = []
            nums.sort()
            backtrack(0)
            return ans


        def sol3(nums):

            res=[]
            n=len(nums)
            def dfs(path,k):
                if k==n-1:
                    res.append(path[:])
                    return
                for i in range(k,n):
                    if i>k and (path[i]==path[k]) :
                        continue
                    if i>k:
                        # here we have changed th value for k , so wont be exploring the
                        # cases where where start index have same values
                        path[i],path[k]=path[k],path[i]
                        dfs(path[:],k+1)
                        # here if we use replacement thing then we
                        # will be  having having previous values for start position
                        # ex 1122
                        # supoose we have explored for first 2[index 2] means for [2112] and if after backtrack 
                        # we reset the values[1122][result of below line] now method will explore for index 3 means for [2112] again
                        # resulting in duplicate elements  so using dfs not backtrack
                        #path[i],path[k]=path[k],path[i]
                    elif i==k:
                        dfs(path[:],k+1)
            nums=sorted(nums)       
            dfs(nums,0)
            return res

        def sol4(nums):
            res=[]
            perm=[]
            # create a dictionary to count how many elements
            count={n:0 for n in nums}
            for n in nums:
                count[n]+=1

            def dfs():
                #Than means we reached where all the elements are used in perm
                if len(nums)==len(perm):
                    return res.append(perm.copy())
                
                for n in count:
                    #If the number still has quota, then we add it into the combination
                    if count[n]>0:
                        perm.append(n)
                        count[n]-=1

                        dfs()
                        #then back track and put the number back
                        count[n]+=1
                        #This combination does not work, then pop it out
                        perm.pop()
            dfs()
            return res

        return sol4(nums)