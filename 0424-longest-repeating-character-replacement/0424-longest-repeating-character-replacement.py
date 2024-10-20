class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
            res = 0
            ch_dict = {} # key,value = ch: last pos
            l = 0
            
            max_freq = 0
            for r, ch in enumerate(s):
                ch_dict[ch] =  ch_dict.get(ch,0)+1
                max_freq = max(max_freq, ch_dict[ch])
                is_valid = (r-l+1 - max_freq <=k)
                #print(ch_dict, l)
                if not is_valid:
                    ch_dict[s[l]]-=1
                    l+=1

                res = max(res, r - l + 1)
            return res


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
            res = 0
            ch_dict = {} # key,value = ch: last pos
            l = 0
            
            max_freq = 0
            for r, ch in enumerate(s):
                ch_dict[ch] =  ch_dict.get(ch,0)+1
                max_freq = max(max_freq, ch_dict[ch])
                is_valid = (r-l+1 - max_freq <=k)
                #print(ch_dict, l)
                if not is_valid:
                    ch_dict[s[l]]-=1
                    l+=1

                res =  r - l + 1
            return res
        


      
        