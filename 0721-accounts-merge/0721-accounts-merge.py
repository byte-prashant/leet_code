class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        dp = {}
        new_account = accounts[:]
        parent = [i for i in range(len(accounts))]
        def find(node):
            if parent[node]!= node:
                parent[node] = find(parent[node])
            return parent[node]

        for idx,account in enumerate(accounts):
            for email in account[1:]:
                if email in dp:
                    node= dp[email]

                    p_node = find(node)
                    parent[find(idx)] = p_node
    
                dp[email] = idx

                    
                
     
        
        # new_account= {}
        # print(parent)
        # print(dp)
        # for index,value in enumerate(parent):
        #     if value in new_account:
        #         new_account[value][0].extend(accounts[index][1:])
        #     else:
        #         new_account[value] = [accounts[index][1:],accounts[index][0]]
        # ans = []

        # print(new_account)
        # for key,value in new_account.items():

            
        #     item = list(set(value[0]))
        #     item.sort()
        #     ans.append([value[1], *item])
        ans = collections.defaultdict(list)
        for email, owner in dp.items():
            ans[find(owner)].append(email)
        
        return [[accounts[i][0]] + sorted(emails) for i, emails in ans.items()]
        return ans





        
       


        