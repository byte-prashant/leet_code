class Solution:
    def longestValidParentheses(self, s: str) -> int:

        def is_valid(st):
           
            count = 0
            for s in st:
                if s=="(" and count<len(st):
                    count+=1
                elif s==")" and count:
                    count-=1
                else:
                    return False
            return not count

        def valid_subseq():

            # the followinng solution is for subsequence
           

            # As we need to find the longest  valid substring
            # means we will be deleting minimum possible character
            # that minimum deletion refers to shallow depth of recursion tree
            # that further means we should use BFS
            q = [(s,0)]
            ans=[]
            while q:

                st , last_pos = q.pop(0)

                if is_valid(st):
                    ans.append(st)
                    return len(st)

                for k in range(last_pos,len(st)):
                    if not k  or (st[k-1]!=st[k]):
                        q.append((st[:k]+st[k+1:],last_pos))

            return 0


        # trying with each substring
        # tle, we can use DP
        # no success after even DP
        def valid_substring_dp():

            max_len = 0
            dp = {}
            for i in range(0,len(s)):
                for j in range(i,len(s)+1):
                    if s[i:j] and s[i:j] in dp:
                        max_len = max(max_len,dp[s[i:j]])
                    if is_valid(s[i:j]):
                        

                        max_len = max(max_len,len(s[i:j]))
                        if s[i:j]:
                            dp.update({s[i:j]:max_len})
            return max_len

        
        def valid_substring_stack():
            max_len = 0
            stack = [-1]
            for i in range(len(s)):
                if s[i] == "(":
                    stack.append(i)
                else:
                    if stack:
                        stack.pop()
                    if not stack:
                        stack.append(i)
                    else:

                        max_len = max(max_len, i-stack[len(stack)-1])

            return max_len



        def valid_substring_stack():
            max_len = 0
            stack = [-1]
            for i in range(len(s)):
                if s[i] == "(":
                    stack.append(i)
                else:
                    if stack:
                        stack.pop()
                    if not stack:
                        stack.append(i)
                    else:
                        max_len = max(max_len, i-stack[len(stack)-1])

            return max_len




        


        return valid_substring_stack()



            
            










