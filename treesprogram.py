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

        if not self.root:  # is self.root is not none
            self.root = Node
            return
        parentnode = self.findparentnode(parentdata,self.root)
        if not parentnode:
            print("parentnode is not found")
            return


        parentnode.children.append(Node)    



    def findparentnode(self,par_data,node):
        if node.data == par_data:
            return node
        
            

