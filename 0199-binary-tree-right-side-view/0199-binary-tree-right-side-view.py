# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue  = [root]
        right_view = []
        new_level = []
        while queue:
            node = queue.pop(0)
            if node.left:
                new_level.append(node.left)
            if node.right:
                new_level.append(node.right)
            if not queue:
                right_view.append(node.val)
                queue = new_level[:]

                new_level= []
        return right_view