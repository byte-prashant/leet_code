class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:

        class UF:
            def __init__(self,n): self.p = list(range(n))

            def union(self,x,y): self.p[self.find(x)] = self.find(y)

            def find(self,x):
                if self.p[x]!=x:
                    self.p[x] = self.find(self.p[x])
                return self.p[x]

        uf = UF(len(s))
        ans = []
        components =  defaultdict(list)

        for x,y in pairs:
            uf.union(x,y)

        for i in range(len(s)):
            components[uf.find(i)].append(s[i])

        for i in range(len(s)):
            components[i].sort(reverse =True)
        
        for i in range(len(s)):
            ans.append(components[uf.find(i)].pop())

        return "".join(ans)
        

