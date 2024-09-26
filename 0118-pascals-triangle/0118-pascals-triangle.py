class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        def sol(k):
            ans =[[1]]
            # if k>=2:
            #     ans =[[1],[1,1]]
            while(k>1):

                row = [1]
                prev_row = ans[-1]
                for index in range(1,len(ans[-1])):
                    row.append(prev_row[index-1]+ prev_row[index])
                row.append(1)

                ans.append(row)
                k-=1

            return ans

        return sol(numRows)
                

        