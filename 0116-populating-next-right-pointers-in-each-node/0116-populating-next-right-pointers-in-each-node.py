"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':

        hashmap =  defaultdict(list)

        def sol(root,level):
            if not root:
                return

            hashmap[level].append(root)
            sol(root.left,level+1)
            sol(root.right,level+1)

        sol(root,1)
        for level in range(1, len(hashmap)+1):
            prev = None
            for node in hashmap[level]:
                if prev:
                    prev.next = node
                prev = node
            hashmap[level][-1].next = None

        return root

        
                



            