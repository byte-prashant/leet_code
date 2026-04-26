class Solution:
    def isPalindrome(self, s: str) -> bool:

        filtered_ch = filter(lambda ch : ch.isalnum(),s)
        lowercase_filtered = map(lambda ch: ch.lower(),filtered_ch)
        list_ch =  list(lowercase_filtered)

        return list_ch == list_ch[::-1]