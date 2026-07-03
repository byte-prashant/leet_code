class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        import copy
        word_dict = {word:0 for word in wordDict}

        def sol( new_s,word_dict):
            if not new_s:

                if all(val for key, val in word_dict.items()):
                    return True

                return False

            
            is_found = False

            for index in range(len(new_s)):
                word1, word2  = new_s[:index],new_s[index:]
                if word1 in word_dict:
                    word_dict[word1] =1

                if word2 in word_dict:
                    word_dict[word2] =1
                new_w_d = copy.deepcopy(word_dict)
                is_found = is_found or sol(word1,new_w_d) or sol(word2,new_w_d)

            return is_found
        return sol(s,word_dict)

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        def sol(current_string):
            if len(current_string)>len(s):
                return False

            if current_string == s:
                return True

            is_found = False
            for word in wordDict:

                is_found = is_found or sol(current_string+word)

            
            return is_found


        return sol("")

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = {}
        def sol(current_string):
            if len(current_string)>len(s):
                return False

            if current_string == s:
                return True

            if current_string in dp:
                return dp[current_string]

            is_found = False
            for word in wordDict:

                is_found = is_found or sol(current_string+word)

            dp[current_string] = is_found
            return dp[current_string]


        return sol("")

      
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        import copy
        dp = {}
        def sol(start, end):

            if (start, end ) in dp:
                return dp[(start,end)]
            if s[start:] in wordDict:
                return True

            if end<=start:
                return False


            is_found = False

            for k in range(start,end):

                if s[ start:k+1] in wordDict and sol(k+1,end):
                    is_found = True

            dp[(start,end)] = is_found

            return dp[(start,end)]

            
        return sol(0, len(s))

        