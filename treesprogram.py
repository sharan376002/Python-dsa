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

        for child in node.children:
            nodefound = self.findparentnode(par_data, child)
            if  nodefound:
                return nodefound

        return None     
    # for remove the value from the node
    def remove(self,data):
        if not self.root:
            print("The tree is empty")
        if self.root.data == data:
            self.root = None
            return
        parentnode = self.findparentnoderm(data.self.root)

    def findparentnoderm(self,data,node):
               
        
    

    def display(self,depth=0, node=None):
        if not node:
            node = self.root
        print(" " * depth+str(node.data)) 
        for child in node.children:
            self.display(depth+1,child)   




t1 = Tree()
t1.Add(1)
t1.Add(2,1)
t1.Add(3,1)
t1.Add(4,2)
t1.Add(5,3)
t1.Add(6,4)
t1.Add(7,4)
t1.display()

