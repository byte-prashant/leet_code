# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        node_to_index = dict(zip(inorder,range(len(inorder))))

        def tree(start,end):
            if start>end:
                return None
            val = postorder.pop()
            node = TreeNode(val)
            mid = node_to_index[val]
            node.right = tree(mid+1,end)
            node.left= tree(start,mid-1)
            return node

        return tree(0,len(inorder)-1)
        