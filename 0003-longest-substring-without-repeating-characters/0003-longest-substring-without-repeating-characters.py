class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:


        def sol():
            dp = {}
            max_len = 0
            lo =hi =0
            while(hi<len(s)):
                if s[hi] in dp:
                    tem = dp[s[hi]]
                    while(lo<=tem):
                        del dp[s[lo]]
                        lo+=1
                max_len = max(max_len, hi-lo+1)
                dp[s[hi]] = hi
                hi+=1
            return max_len

        def sol():
            dp ={}
            max_len = 0
            lo = hi =0
            while(hi<len(s)):

                if s[hi] in dp:
                    new_pos = dp[s[hi]]
                    while(lo<=new_pos):
                        del dp[s[lo]]
                        lo+=1

                max_len = max(max_len, hi-lo+1)
                dp[s[hi]] = hi
                hi+=1
            return max_len

        def sol():
            print("oi")
            str_len = len(s)
            dp = {}
            ans =0
            i=0
            for j  in range(len(s)):
                if s[j] in dp:
                    # to ignore the previuos seen character
                    i = max(dp[s[j]],i)

                ans = max(ans, j-i+1)
                dp[s[j]] = j+1


            return ans

        def sol():
           
            dp = {}
            ans = 0
            left = 0
            for right in range(len(s)):
                
                if s[right] in dp:

                    left = max(dp[s[right]]+1,left)
                ans = max(ans,right-left+1)

                dp[s[right]] = right

           

            return ans

        def sol():

            dp = {}
            ans = 0
            left = 0
            for right, ch in enumerate(s):

                if not ch in dp or dp[ch]<left:

                    ans = max(ans,right - left+1)

                else:
                    left  = dp[ch]+1
                dp[ch] = right

            return ans
                    

        return sol()
        