class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        def sol():
            dp = {}
            max_len = 0
            hi =lo = 0
            dis = 0
            while(hi<(len(s)) and k):

                if s[hi] in dp:
                    dp[s[hi]]+=1
                else:
                    dp[s[hi]]=1
                    dis+=1
                    if dis>k:
                        while(lo<hi and dis>k):
                            c = dp[s[lo]]-1
                            if c>0:
                                dp[s[lo]]-=1
                            else:
                                dis-=1
                                del dp[s[lo]]

                            lo+=1
                
                max_len = max(max_len, hi-lo+1)
                hi+=1

            return max_len

        def sol(s,k):
            dis = k
            max_size = 0
            left = 0
            dp = collections.Counter()
            for right in range(len(s)):

                if not s[right] in dp:
                    dis-=1

                dp[s[right]]+=1
                
                if dis>=0:
                    max_size = max(max_size, right-left+1)
                else:
                    dp[s[left]]-=1
                    if  dp[s[left]] ==0:
                        del dp[s[left]]
                        dis+=1
                    left+=1
                    
                    
           
            return max_size
# above dis variable only tells the len of dp[unique chars]
# so we can replaace it
# and also think if we can remove the left pointer
# left pointer = right - max_size


        def sol(s,k):
            max_size = 0
            left = 0
            dp = collections.Counter()
            for right in range(len(s)):


                dp[s[right]]+=1
                    
                if len(dp)<=k:
                    max_size = max_size+1
                else:
                    dp[s[right-max_size]]-=1
                    if  dp[s[right-max_size]] ==0:
                        del dp[s[right-max_size]]
           
            return max_size


# nice solution amazing
        def sol1(s,k):
            res = 0
            ch_dict = collections.defaultdict(int) # key,value = ch: last pos
            l = 0
            for r, ch in enumerate(s):
                ch_dict[ch] = r
                #print(ch_dict, l)
                while len(ch_dict) > k:
                    if ch_dict[s[l]] == l:
                        del ch_dict[s[l]]
                    l += 1
                res = max(res, r - l + 1)
            return res

        


        return sol(s,k)


        