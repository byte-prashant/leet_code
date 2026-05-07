class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        

        ans = {}
        def comb(subset,pos):
            if len(subset)==k:
                ans[tuple(sorted(subset[:]))] =1
                return

            for value in range(pos,n+1):
                subset.append(value)
                comb(subset,value+1)
                subset.pop(-1)

            return
        comb([],1)

        return [list(key) for key,value in ans.items()]

