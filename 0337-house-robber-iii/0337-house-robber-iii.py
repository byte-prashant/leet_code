# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:


        def sol(root, pick):

            if not root:
                return 0

            val = 0
            if pick:
                
                val = max( sol(root.left,0)+root.val+sol(root.right,0), sol(root.left,1)+sol(root.right,1))
            else:
               

                val+=sol(root.left,1)
                val+=sol(root.right,1)


            return val

        return max(sol(root,True),sol(root,False))


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # Message Passing function
        def dfs(node):
            if not node:
                # Base case: (Max if not robbed, Max if robbed)
                return (0, 0)
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            # If we DON'T rob this node, we can choose to rob 
            # or not rob the children (take the max of each)
            not_robbed = max(left) + max(right)
            
            # If we DO rob this node, we MUST NOT rob the children
            robbed = node.val + left[0] + right[0]
            
            return (not_robbed, robbed)
        
        return max(dfs(root))        