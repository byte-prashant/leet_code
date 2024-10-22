# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        money = 0
        node = root
        dp  = {}
        def bt(node,pick):
            if (node,pick) in dp:
                return dp[(node,pick)]
            if not node:
                return 0

            m = 0
            if  pick:
                    m = max( bt(node.left,0)+node.val+bt(node.right,0), bt(node.left,1)+bt(node.right,1))

            else:
                m = bt(node.left,1)+bt(node.right,1)
            
            dp.update({(node,pick):m})
            return m

        return max(bt(root,0),bt(root,1))


            


                
