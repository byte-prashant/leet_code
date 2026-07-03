class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        dp = {}
        ans = []
        def sol(start, end, word_list):
            # if (start, end) in dp:
            #     return dp[(start,end)]

            if end<=start:
                j= " ".join(word_list)
                ans.append(j)
                return

            for k in range(start,end):

                if s[start:k+1] in wordDict:
                    
                    word_list.append(s[start:k+1])
                    sol(k+1,end,word_list )
                    word_list.pop(-1)

            return

        sol(0, len(s), [])

        return ans

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        dp = {}
        ans = []
        def sol(start, end):
            if (start, end) in dp:
                return dp[(start,end)]

            results = []
            if end<=start:
                
                results.append("")
                return results

            for k in range(start,end):

                if s[start:k+1] in wordDict:
                    
                    word = s[start:k+1]
                    sub_list = sol(k+1,end )
                    for sub in sub_list:

                        if sub:
                            results.append(f"{word} {sub}")
                        else:
                            results.append(word)

                    

            dp[(start,end)] = results

            return   dp[(start,end)]

      

        return    sol(0, len(s)) 