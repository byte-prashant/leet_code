class Solution:
    def minWindow(self, s: str, t: str) -> str:

        required_dict = Counter(t)

        formed =0
        formed_dict = {}
        lo = hi =0
        ans = float("inf"), None, None
        while hi < len(s):

            ch = s[hi]
            formed_dict[ch ] = formed_dict.get(ch,0)+1
           
            if ch in required_dict and formed_dict[ch] == required_dict[ch]:
                formed+=1
            
            while formed == len(required_dict) and lo<=hi:
                ch = s[lo]
                if hi-lo+1< ans[0]:
                    ans = (hi-lo+1, lo, hi)
    
                formed_dict[ch]-=1
                if s[lo] in required_dict:
                    
                    if formed_dict[ch] < required_dict[ch]:
                        formed-=1

                lo+=1

            hi+=1

        return "" if ans[0]==float('inf') else s[ans[1]:ans[2]+1]

    def minWindow(self, s: str, t: str) -> str:
        req_dict = Counter(t)
        #print(dict(req_dict))

        win_elem = {}
        right = 0
        left = 0
        cur_length = 0
        ans  = (float("+inf"),[0,0])
        while(right<len(s)):
            ch = s[right]

           
            win_elem[ch] = win_elem.get(ch,0)+1

            if ch in req_dict and win_elem[ch] == req_dict[ch]:
                cur_length+=1
                
           
            #print(dict(req_dict) == win_elem,win_elem)
            while cur_length == len(req_dict) and left<=right:
               
                char = s[left]
                #ans = min(ans, right-left)
                print(ans)
                if ans[0]>right-left+1:
                    ans = (right-left+1,[left,right])

                win_elem[char]-=1
                
                # if win_elem[char] == 0:
                #    del win_elem[char]
                if char in req_dict:
                    if win_elem[char]<req_dict[char]:
                        cur_length-=1
                
                left+=1
            
            right+=1
        return s[ans[1][0]:ans[1][1]+1] if ans[0]!=float("+inf") else ""


        