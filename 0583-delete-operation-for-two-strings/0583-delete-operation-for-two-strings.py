class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        dp={}
        def common_sub(i,j):

            if i>= len(word1) or j>=len(word2):
                return 0

            
            if (i,j) in dp:
                return dp[(i,j)]

            
            if word1[i] == word2[j]:

                dp[(i,j)] = common_sub(i+1,j+1)+1
            
            else:
                dp[(i,j)] = max(common_sub(i+1,j),common_sub(i,j+1))


            
            return dp[(i,j)]

        comm = common_sub(0,0)

        return len(word1)-comm+len(word2)-comm