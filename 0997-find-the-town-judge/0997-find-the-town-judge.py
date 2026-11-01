class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:

        trust_indegree = [0 for _ in range(n)]
        out_degree = [0 for _ in range(n)]
        for p_a, p_b in trust:
            trust_indegree[p_b-1]+=1
            out_degree[p_a-1]+=1


        migth_be_judge = -1

        for person in range(n):
            if n-1 == trust_indegree[person]:
                migth_be_judge = person
                break
        
        if migth_be_judge>-1 and out_degree[migth_be_judge]==0:
            return migth_be_judge+1

        return -1



        