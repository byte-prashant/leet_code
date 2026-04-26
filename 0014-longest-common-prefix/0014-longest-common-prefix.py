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

# checkout
# create docker image
# push image to ecr (elastic contaoner registry)
# scanning for vulnerability
# sonar quebe
# git hub actions
# ecs 

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


        strs = sorted(strs, key = lambda x : len(x))
        print(strs)
        min_len = len(strs[0])
        count = 0
        while(count<min_len):

            if strs[0][count] == strs[-1][count]:
                count+=1

            else:
                break

        return strs[0][0:count]
        
        

    def longestCommonPrefix(self, strs: List[str]) -> str:
            strs.sort(key=lambda x: len(x))
            count = 0
            print(strs)
            while count<len(strs[0]) and strs[0]!="":
                for string in strs[1:]:
                    if strs[0][count] != string[count]:
                        return strs[0][:count] if count else ""
                count+=1
            return strs[0][:count] if count else ""
                        
        