class Solution:
    def countAndSay(self, n: int) -> str:

        s = "1"
        n =n-1
        while n>0:
            #print(n,s)
            new_s = ""
            count = 0
            prev = ""
            stack = False
            for ch in s:
                #print(new_s)
                if not prev:
                    prev =  ch
                    count+=1
                    stack = False
                elif prev == ch:
                    count+=1
                    stack = False

                else:
                    new_s+=str(count)+prev
                    prev = ch
                    count = 1
                    

            
            new_s+=str(count)+prev

            s = new_s 
            n-=1

        return s
        