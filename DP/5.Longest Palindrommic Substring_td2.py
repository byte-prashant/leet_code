from functools import cache


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # each palindromic substring contains a smoller one..
        start, end = self.help((0, len(s)), s)
        return s[start:end]

    @cache
    def help(self, subrange: tuple[int, int], s: str) -> tuple[int, int]:
        # all len-1 & len-0 substrings are palindromes
        start, end = subrange
        if end - start <= 1:
            return subrange

        interior = (start + 1, end - 1)
        if s[start] == s[end - 1] and self.help(interior, s) == interior:
            return subrange

        left_max = self.help((start, end - 1), s)
        right_max = self.help((start + 1, end), s)

        return max(left_max, right_max, key=lambda r: r[1] - r[0])