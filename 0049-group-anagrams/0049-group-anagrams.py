class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dp = {}
        groups = []
        for index in range(len(strs)):
            #print(dp,groups)
            curr_ana = strs[index]
            curr_ana = "".join(sorted(curr_ana))
            #print(curr_ana)
            if curr_ana in dp:
                group_index = dp[curr_ana]
                groups[group_index].append(strs[index])

            else:
                groups.append([strs[index]])
                pos = len(groups)-1
                dp[curr_ana] = pos

        return groups


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dp = defaultdict(list)

        for s in strs:
            new_str = "".join(sorted(s))
            dp[new_str].append(s)


        return list(dp.values())

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        from collections import defaultdict

        anagrams = defaultdict(list)

        for word in strs:
            count = [0]*26
            for ch in word:
                count[ord(ch)-ord("a")]+=1
            count = tuple(count)
            anagrams[count].append(word)

        return list(anagrams.values())
                




