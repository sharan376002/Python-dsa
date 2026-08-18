# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True
        
        
        root_val = root.val
        
        
        if root.left:
            if root.left.val >= root_val:
                return False
        if root.right:        
            if  root.right.val <= root_val:
                return False
            

        l = self.isValidBST(root.left)
        r = self.isValidBST(root.right)

        if not l or not r:
            return False

       
        return True
        
