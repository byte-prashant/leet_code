def longestPalindrome(self, s: str) -> str:
    if s is "":
        return ""

    rev = s[::-1]
    dp = [[0 for i in range(len(s))] for j in range(len(s))]
    max_len = 0
    max_end = 0
    for i in range(len(s)):
        for j in range(len(s)):
            if s[i] == rev[j]:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    ## dependant on just previous row
            if dp[i][j] > max_len:
                if i - dp[i][j] + 1 == len(s) - 1 - j:
                    max_len = dp[i][j]
                    max_end = i

    return s[max_end - max_len + 1: max_end + 1]


# space optimized


class Solution1_update:
    def longestPalindrome(self, s: str) -> str:
        if s is "":
            return ""
        rev = s[::-1]
        dp = [0 for i in range(len(s))]
        max_len = 0
        max_end = 0
        for i in range(len(s)):
            # Updated the loop order
            for j in range(len(s) - 1, -1, -1):
                if s[i] == rev[j]:
                    if i == 0 or j == 0:
                        dp[j] = 1
                    else:
                        dp[j] = dp[j - 1] + 1
                # Updated here - new columns should be updated on conditions
                else:
                    dp[j] = 0
                if dp[j] > max_len:
                    if i - dp[j] + 1 == len(s) - 1 - j:
                        max_len = dp[j]
                        max_end = i

        return s[max_end - max_len + 1: max_end + 1]
