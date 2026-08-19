# A single node in the tree
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def inorderTrvasal(self,root):

        rs = []
        k  = 3

        if not root:
            return []

        rs+= self.inorderTrvasal(root.left)

        rs.append(root.val)

        rs+= self.inorderTrvasal(root.right)


        
        return rs
            






# Create the nodes
root = TreeNode(5)

root.left = TreeNode(3)
root.right = TreeNode(6)

root.left.left = TreeNode(2)
root.left.right = TreeNode(4)

root.left.left.left = TreeNode(1)


travsal =  root.inorderTrvasal(root)
print("output ", travsal)

k  =3

print(travsal[k-1])
#root.right.left = TreeNode(7)
#root.right.right = TreeNode(10)