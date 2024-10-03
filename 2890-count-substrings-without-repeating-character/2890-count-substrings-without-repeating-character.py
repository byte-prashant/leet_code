class Solution:
    def numberOfSpecialSubstrings(self, s: str) -> int:

        hash_map = {}

        left =0
        right = 0

        count = 0

        while(right<len(s)):

            if s[right] in hash_map:

                left= max(left,hash_map[s[right]]+1)


            count+=right-left+1
            hash_map[s[right]]= right
            right+=1

        return count


        