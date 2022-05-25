class Solution3:
    def longestPalindrome(self, s: str) -> str:
        if s is "":
            return s
        res = ""
        dp = [None for i in range(len(s))]
        for j in range(len(s)):
            for i in range(j+1):
                if i == j:
                    dp[i] = True
                elif j == i+1:
                    dp[i] = (s[i] == s[j])
                else:
                    dp[i] = (dp[i+1] and s[i] == s[j])
                if dp[i] and j - i + 1 > len(res):
                    res = s[i:j+1]
        return res


###########################################
class Solution3:
    def longestPalindrome(self, s: str) -> str:
        if s is "":
            return s
        res = ""
        dp = [[None for i in range(len(s))] for j in range(len(s))]
        for j in range(len(s)):
            for i in range(j+1):
                if i == j:
                    dp[j][i] = True
                elif j == i+1:
                    dp[j][i] = (s[i] == s[j])
                else:
                    dp[j][i] = (dp[j-1][i+1] and s[i] == s[j])
                if dp[j][i] and j - i + 1 > len(res):
                    res = s[i:j+1]
        return res
