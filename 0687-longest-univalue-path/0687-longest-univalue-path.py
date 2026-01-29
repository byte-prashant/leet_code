# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        max_path = 0
        def dfs(node):
            nonlocal max_path
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
            l=r= 0
            if node.left and node.left.val == node.val:
                l = left+1

            if node.right and node.right.val == node.val:
                r=right+1

            max_path = max(max_path,l+r)

            return max(l,r)

        dfs(root)
        return max_path

           
        