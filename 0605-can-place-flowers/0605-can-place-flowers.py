class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        # brute force
        def sol1(self,flowerbed,n):
            if n ==0:
                    return True
            if len(flowerbed)==1:
            
                if n==1:
                    if flowerbed[0]==0:
                        return True
                return False
            # brute force
            for i in range(len(flowerbed)):
                m = n
                for j in range(i,len(flowerbed),2):
                    if flowerbed[j] ==0 :
                        if (j==0 and flowerbed[j+1]!=1 ) or (j==len(flowerbed)-1 and flowerbed[j-1]!=1) or ( flowerbed[j-1]!=1 and flowerbed[j+1]!=1 ):
                            m -=1
                    if not m:
                        return True
            return False

        def sol2(self, flowered, n):
            if n ==0:
                return True
            
            if len(flowerbed)==1:
            
                if n==1:
                    if flowerbed[0]==0:
                        return True
                return False
                
            m=n
            for j in range(0,len(flowerbed),1):
                if flowerbed[j] ==0 :
                    if (j==0 and flowerbed[j+1]!=1 ) or (j==len(flowerbed)-1 and flowerbed[j-1]!=1) or ( flowerbed[j-1]!=1 and flowerbed[j+1]!=1 ):
                        m -=1
                        flowerbed[j]=1
                if not m:
                    return True
            return False

        return sol2(self,flowerbed,n)


        