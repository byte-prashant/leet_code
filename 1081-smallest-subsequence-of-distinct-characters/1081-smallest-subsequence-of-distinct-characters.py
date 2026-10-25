class Solution:
    from collections import defaultdict
    def smallestSubsequence(self, s: str) -> str:

        stack = []
        window = defaultdict(int)
        freq = defaultdict(int)
        for ch in s:
            freq[ch]+=1
        
        for index,ch in enumerate(s):
            freq[ch]-=1
            if window[ch]>0:
                continue
            while stack and stack[-1]>ch and  freq[stack[-1]]>0 :
                win_ch = stack.pop()
                window[win_ch]-=1

               

           
            stack.append(ch)
            window[ch]+=1
            print(window, stack)

        return "".join(stack)
        