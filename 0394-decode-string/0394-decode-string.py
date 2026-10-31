class Solution:
    def decodeString(self, s: str) -> str:


        def sol(pos):
            ans = ""
            num = 0

            while pos<len(s):
                ch = s[pos]
                if ch=="[":

                    sub_str,pos = sol(pos+1)
                    if num>0:
                        for _ in range(num):
                            ans+=sub_str
                        num = 0
                    
                    continue
                else:

                    if ch.isdigit():
                        num =num*10+int(ch)

                    elif ch.isalpha():
                        ans+=ch
                    else:

                        return ans,pos+1
                pos+=1

            return ans,pos

        return sol(0)[0]

        