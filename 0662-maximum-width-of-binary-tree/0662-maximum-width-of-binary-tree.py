# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        queue = [(root,0)]
        
        max_width = 0
        while queue:
           
            level_width = len(queue)
            _,start_indx = queue[0]
            end_indx = None
            for i in range(level_width):
                node,pos  = queue.pop(0)
               
                if i == level_width-1:
                    end_indx = pos
              
                if node.left:
                    queue.append((node.left,2*pos))
                if node.right:
                    queue.append((node.right,2*pos+1))
               
           
            max_width = max(max_width,end_indx-start_indx+1)
            
        return max_width