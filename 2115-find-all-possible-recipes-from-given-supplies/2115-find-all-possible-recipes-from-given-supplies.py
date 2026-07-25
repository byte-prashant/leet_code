class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:

        from collections import defaultdict
        graph = defaultdict(list)
        
        dp = {}
        for sup in supplies:
            dp[sup] =1

        for index,rec in enumerate(recipes):
            for ing in ingredients[index]:
                graph[rec].append(ing)
                
        print(graph)
        vec = {rep:0 for rep in recipes}


        def dfs(node):
            if node in dp:
                return dp[node]

            if node not in set(recipes):
                return False

            if vec[node] == 2:
                return dp[node]

            

            if vec[node] ==1:
                return False

            vec[node ] =1
            
            for neigh in graph[node]:

                if not dfs(neigh):
                    dp[node] = False
                    vec[node]  = 2
                    return False

            dp[node] = True
            vec[node]  = 2
            return True

        ans = []
        for rec in set(recipes):
            if dfs(rec):
                ans.append(rec)

        return ans

        



            

