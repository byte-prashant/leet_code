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
        
class Solution:
    def countAndSay(self, n: int) -> str:


        say = "1"
        n = n-1

        while n>0:
            new_say = ""
            prev = None
            left = 0
            right = None
            count = 0
            for right,ch in enumerate(say):
                right = right
                if prev == None or prev==ch:
                    prev = ch
                    count+=1
                else:
                    new_say+= str(count)+prev
                    prev = ch
                    left = right
                    count =1
            
            new_say += str(count)+prev
            say= new_say

            n=n-1
        return say
        

