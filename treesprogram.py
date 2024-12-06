# tree 
 
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []


class Tree:
    def __init__(self):
        self.root = None

    def Add(self,data,parentdata=None):
        Node = TreeNode(data)    