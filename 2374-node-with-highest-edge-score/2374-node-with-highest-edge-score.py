class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        score_data = [0 for _ in range(len(edges))]

        for node1, node2 in enumerate(edges):

            score_data[node2]+=node1

        score_data =[(node,score ) for node, score in enumerate(score_data) ]
        
        score_data.sort(key= lambda x :(- x[1],x[0] ) )
        ans =  score_data[0]
        pos = 1
        # print(score_data)
        # while pos<len(score_data) and score_data[pos][1]== ans[1] and score_data[pos][0]=> ans[0]:
        #     ans = score_data[pos]
        #     pos+=1

        return ans[0]

