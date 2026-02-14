# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        self.pos = -1
        inorder_d=val_to_index = dict(zip(inorder, range(len(inorder))))

        def get_tree(start,end):
            if start>end:
                return None
            if self.pos+1 > len(preorder)-1:
                return  None
            self.pos = self.pos+1
            val = preorder[self.pos]
            new_node =  TreeNode(val,None,None)
            mid = inorder_d[val]
            
            new_node.left  = get_tree(start,mid-1)
            new_node.right = get_tree(mid+1,end)
            print(type(new_node))
            return new_node

        return get_tree(0,len(preorder))
