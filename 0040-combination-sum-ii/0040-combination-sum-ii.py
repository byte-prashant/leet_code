import copy
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        pattern = []
        candidates.sort()
        def combination(i,subset):

            if sum(subset)==target:
                pattern.update({tuple(subset):1})

            if i>=len(candidates):
                return 

            for k in range(i,len(candidates)):
                # following a main concept to avoid the similar subset again
                if k > i and candidates[k] == candidates[k-1]:
                    continue
                subset.append(candidates[k])
                combination(k+1,subset)
                subset.pop(-1)

            return 

        # above solution giving TLE,introducing new var sum, to find sum continuously
        # still giving the TLE
        # after introducing following condition, i got success
        # if summ > target:
        #         return
        def combination(i,subset,summ):

            if summ==target:
                pattern.update({tuple(subset):1})
            if summ > target:
                return
            if i>=len(candidates):
                return 

            for k in range(i,len(candidates)):
                if k > i and candidates[k] == candidates[k-1]:
                    continue
                
                subset.append(candidates[k])
                summ+=candidates[k]
                combination(k+1,subset,summ)
                summ-=candidates[k]
                subset.pop(-1)

            return 



        def combination(i,subset,summ):

            if summ==target:
                pattern.append(subset)
            if summ > target:
                return
            if i>=len(candidates):
                return 

            for k in range(i,len(candidates)):
                if k > i and candidates[k] == candidates[k-1]:
                    continue
                combination(k+1,subset+[candidates[k]],summ+candidates[k])
            
            return 


        combination(0,[],0)
        
        return pattern


        def combination(i,subset,summ):

            if summ==target:
                pattern.append(subset)
            if summ > target:
                return
            if i>=len(candidates):
                return 

            for k in range(i,len(candidates)):
                if candidates[k] == candidates[k-1]:
                    continue
                combination(k+1,subset+[candidates[k]],summ+candidates[k])
            
            return 

        candidates.sort()

        combination(0,[],0)
        
        return pattern

