class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if beginWord == endWord:
            return []
        
        if endWord not in wordList:
                return []

           
    
            
        def diff_1(first, second):
                #print(zip(first, second))
                delta = 0
                for a, b in zip(first, second):
                    if a != b:
                        if delta == 1:
                            return False
                        delta += 1
                return True
            
        vs = defaultdict(list)
        for u, a in enumerate(wordList):
            for v in range(0, len(wordList)):
                if diff_1(a, wordList[v]):
                    vs[a].append(wordList[v])

        # adding starting word to adjacency list
        if not beginWord  in vs:
            for v in  wordList:
                if diff_1(beginWord, v):
                        vs[beginWord].append(v)

        
       # print(vs)
        queue = [[beginWord]]
        ans = []
        shortest_path = float("inf")
        while queue:
          
            length =  len(queue)
            delete_node= []
            next_level = []
            for i in range(length):
                path = queue.pop(0)
              
                last_node = path[-1]

               
                if last_node == endWord:
                        if shortest_path > len(path):
                            ans = [path[:]]
                            shortest_path = len(path)
                        elif shortest_path == len(path):
                            ans.append(path[:])
                else:
                    
                    if last_node in  vs and vs[last_node]:
                        delete_node.append(last_node)
                        for new_node in vs[last_node]:
                            new_path = path[:]
                            new_path.append(new_node)
                            next_level.append(new_path)
            for node in set(delete_node):
                del vs[node]
            queue=next_level
      

        return ans
                


    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        from collections import defaultdict
        wordSet = set(wordList)  # to check if a word is existed in the wordSet, in O(1)
        wordSet.discard(beginWord)

        def neighbour(word):
            for i in range(len(word)):
                for c in ascii_lowercase:
                    new_word  = word[:i]+c+word[i+1:]
                    if new_word in wordSet:
                        yield new_word

        

        level = {}
        level[beginWord] = [[beginWord]]

        while level:
            next_level = defaultdict(list)

            for word, paths in level.items():
                if word == endWord:
                    return paths

                
                for neigh in neighbour(word):
                    for path in paths:
                        new_path = path[:]
                        new_path.append(neigh)
                        next_level[neigh].append(path+[neigh])
            wordSet-=set(next_level.keys())
            level = next_level

        return []
            
    

                

    # below is level order, converting it queue
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        from collections import defaultdict

        word_set = set(wordList)

        level = [[beginWord]]
        
        ans= []
        while level:
            next_level = []

            for path in level:
                word_set.discard(path[-1])

            for path in level:
                if path[-1] == endWord:
                    if not ans:
                        ans.append(path)
                    elif len(ans[0]) == len(path):
                        ans.append(path)



            for path in level:
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    word = path[-1]
                    for pos in range(len(path[-1])):
                        new_word = word[:pos] + ch + word[pos+1:]
                        if new_word in word_set:
                            new_path = path[:]
                            new_path.append(new_word)
                            next_level.append(new_path)
            level = next_level
           

        return ans

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)  # Fast lookup and deletion
        queue = deque([[beginWord]])  # Each element is a path (list of words)
        used_on_level = [beginWord]
        level = 0
        ans = []

        while queue:
            path = queue.popleft()

            # Remove used words when moving to the next BFS level
            if len(path) > level:
                level += 1
                for word in used_on_level:
                    word_set.discard(word)

            word = path[-1]

            # If we found the target word
            if word == endWord:
                if not ans:
                    ans.append(path[:])
                elif len(ans[0]) == len(path):
                    ans.append(path[:])

            # Try changing each character of the current word
            for i in range(len(word)):
                original = word[i]
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = word[:i] + c + word[i+1:]
                    if new_word in word_set:
                        path.append(new_word)
                        queue.append(path[:])
                        used_on_level.append(new_word)
                        path.pop()
        
        return ans

                        
                      

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
       # from collections import defaultdict
        neigh =  defaultdict(list)

        # find all neghbours
        # then reverse back track from target to start

        word_set = set(wordList)
        level = [beginWord]
        found = False
        while level and not found:
            next_level = set()

            for ele in level:
                word_set.discard(ele)


            
            for ele in level:
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    for pos in range(len(ele)):

                        new_word = ele[:pos]+ch+ele[pos+1:]
                        if new_word in word_set:
                            neigh[new_word].append(ele)
                            next_level.add(new_word)
                            
            if endWord in next_level:
                break

            level = next_level
            

        
        start = [endWord]
        print(neigh)
        ans= []
        def dfs(start,path):

            if path[-1] ==beginWord:
                ans.append(path[::-1])
                return

            
            for ngh in neigh[start]:

                path.append(ngh)
                dfs(ngh,path)
                path.pop()

            return
        
        if endWord in neigh:
            dfs(endWord,[endWord])

        return ans










                        
        

    