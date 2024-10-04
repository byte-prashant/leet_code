class Solution:
    def minWindow(self, s1: str, s2: str) -> str:

        # using subsequence
        dp = {}

        def subseq(pos, t_pos, start, end, min_in):
            if (pos, t_pos, start, end) in dp:
                return
            # print(min_in)
            if t_pos >= len(s2):
                print("in")
                if min_in[0] == end - start + 1:
                    if min_in[1] > start:
                        min_in[1] = start
                        min_in[2] = end

                elif min_in[0] > end - start + 1:
                    min_in[0] = end - start + 1
                    min_in[1] = start
                    min_in[2] = end
                # print("min", min_in)
                dp.update({(pos, t_pos, start, end): 1})
                return min_in

            if pos >= len(s1):
                dp.update({(pos, t_pos, start, end): 1})
                return min_in

            # not_pick

            # pick
            if s1[pos] == s2[t_pos]:
                if start == -1:
                    start = pos
                subseq(pos + 1, t_pos + 1, start, pos, min_in)
            else:
                subseq(pos + 1, t_pos, start, pos, min_in)

            return

        min_in = [float("inf"), None, None]
        for start in range(0, len(s1)):
            subseq(start, 0, -1, -1, min_in)
        return s1[min_in[1] : min_in[2] + 1] if min_in[0] != float("inf") else ""
    


    def minWindow(self, s1: str, s2: str) -> str:
        str1, str2 = s1, s2
        left = right = 0
        count = 0

        min_wind = [float("+inf"), ""]
        while(right<len(str1)):
        
            if str1[right] == str2[count]:
                count+=1
                
            if count  == len(str2):
                start = end = right
                index2 = count-1
                while(index2>=0):
                        if str1[start] == str2[index2]:
                            index2-=1       
                    
                        start-=1
                start += 1
                if min_wind[0] > end- start +1:
                    min_wind = [end- start +1, str1[start:end+1]]
                count =0
                right = start
                
            right+=1 
        return min_wind[1]