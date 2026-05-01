class Solution:
    def compress(self, chars: List[str]) -> int:
        ans = []
        left = right =0
        if len(chars)==1: return 1
        pos = 0
        for right in range(0,len(chars)):

            if chars[left]!=chars[right]:
                
                chars[pos] = chars[left]
                pos+=1
                if right-left>1:
                   
                    for ch  in str(right-left):
                        chars[pos] = ch
                        pos+=1
                  
                #print(pos,left,right,chars)
                left= right

        
        #print(pos,left,right,chars,ans)
            
        
      
        chars[pos] = str(chars[left])
        pos+=1
        if right-left>0:
           
            for ch  in str(right-left+1):
                chars[pos] = ch
                pos+=1
        #print(pos,left,right,chars,ans)
        
        return pos

            
        