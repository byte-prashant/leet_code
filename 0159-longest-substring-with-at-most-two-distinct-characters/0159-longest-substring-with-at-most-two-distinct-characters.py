class Solution:

    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:

        dp = {}
        max_len = 0
        hi =lo = 0
        dis = 0
        while(hi<(len(s))):

            if s[hi] in dp:
                dp[s[hi]]+=1
            else:
                dp[s[hi]]=1
                dis+=1
                if dis>2:
                    while(lo<hi and dis>2):
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




        def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:



            left=right=0
            ans = 0
            hashmap = defaultdict()
            while(right<n):
                hashmap[s[right]] = right

                if len(hashmap) ==3:
                    indx = min(hashmap.values())
                    del hashmap[s[indx]]
                    left= indx+1

                ans = right-left+1

                right+=1

            return ans

        


                




        

        


                

                        



                





        