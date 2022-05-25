class Solution:

    ## need to test it completely
    def maxi(self, x, y):
        if len(x) > len(y):
            return x
        else:
            return y

    def longestPalindrome(self, s: str) -> str:
        k = len(s) - 1
        return self.longPal(s, 0, k)

    def longPal(self, s, i, k):

        dp = {}
        sstr = s[0]
        slen = 1

        def longestPalindromic(strn, i, j):
            nonlocal sstr, slen
            if i > j:
                return True

            if i == j:
                return True

            if (i, j) in dp:
                return dp[(i, j)]

            if strn[i] == strn[j]:
                substr = longestPalindromic(strn, i + 1, j - 1)

                if substr:

                    if slen < j - i + 1:
                        slen = j - i + 1
                        sstr = strn[i:j + 1]
                    return True
            longestPalindromic(strn, i + 1, j)
            longestPalindromic(strn, i, j - 1)

            dp.update({(i, j): False})

            return False

        longestPalindromic(s, i, k)
        return sstr
