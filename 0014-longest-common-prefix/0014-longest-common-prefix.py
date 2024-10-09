class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # if len( strs)==1:
        #     return strs[0]

        # index = 0
        
        # while True:
        #     prev = strs[0][:index+1]
            
        #     for word in strs[1:]:
        #         if word and word[:index+1] == prev and len(word)+1>=index:
        #             continue
        #         else:
        #             return prev[:index] if prev else ""
        #     index+=1


        ans = ""
        for i in range(len(min(strs))):
            s = strs[0][i]
            for j in range(len(strs)):
                if strs[j][i] != s:
                    return ans
            
            ans += s
        
        return ans

        