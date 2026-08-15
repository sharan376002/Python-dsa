# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root):

        rs  =[]

        if not root:
            return rs

        

        rs+= self.postorderTraversal(root.left)
        rs+= self.postorderTraversal(root.right)
        rs.append(root.val)

        return rs
        