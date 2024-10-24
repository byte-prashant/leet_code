# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        elem = [-1]
        result = []
        def sol(root):
            if not root:
                return

            if root.left:
                sol(root.left)

            result.append(root.val)
            

            if root.right:
                sol(root.right)

            return


        sol(root)
        return  result[k-1] if k<=len(result) else -1


# decresing the space complexity

        
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        elem = [-1]
        count = [k]
        def sol(root):
            if not root or count[0]==0:
                return

            if root.left:
                sol(root.left)
           
            count[0]-=1
            if count[0]==0:
                elem[0] = root.val
               

            if root.right:
                
                sol(root.right)

            return


        sol(root)
       
        return elem[0] 




        