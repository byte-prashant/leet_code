class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = {}
        def sol(index, candi):
            print(index, candi)
            if candi and sum(candi)==target:
                res[tuple(candi)]=1
                if not tuple(candi) in res:
                    res[tuple(candi)]=1
                else:
                    print("foun second time")
                return
            if candi and sum(candi)> target:
                return

            if index<0:
                return

            not_select = sol(index-1,candi)
            new_candi = candi[:]
            new_candi.append(candidates[index])
            select = sol(index,new_candi)
            #select = sol(index-1,new_candi[:])

            return

        sol(len(candidates)-1, [])
        return  [keys for keys in res.keys()]

        def sol():
            #candidates.sort()
            ret = []

            def visit(idx, target, arr):
                if target == 0:
                    ret.append(arr[:])
                    return
                elif target < 0:
                    return

                for i in range(idx, len(candidates)):
                    e = candidates[i]
                    if e <= target:
                        visit(i, target - e, arr+[e])
                    else:
                        break

            visit(0, target, [])
            return ret
        #return sol()





        