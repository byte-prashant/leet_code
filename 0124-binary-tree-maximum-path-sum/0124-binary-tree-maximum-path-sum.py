# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        
        ans = [ root.val]

        def sol(root):


            if not root:
                return 0


            left = sol(root.left)
            right = sol(root.right)

            ans[0] = max(ans[0] ,max(left,0)+max(right,0)+root.val)

            return root.val + max(0, left, right)

        sol(root)

        return ans[0]

