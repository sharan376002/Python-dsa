


class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


class Binary_tree:
    def __init__(self):
        self.root = None

    def Add(self,data):
        if not self.root:
            self.root = Node(data)
            return

        self._recursiveadd(data,self.root)

    def _recursiveadd(self,data,node):
        if node.left is None:
            node.left = Node(data)
            return

        elif node.right is None:
            node.right = Node(data)
            return

        else:
             self._recursiveadd(data, node.left)  # we can pass also right side 
             return      

    def Display(self,depth=0,node=None):
        if node is not None:
            node =  self.root

        print(" " * depth * 2, node.data)

        if node.left is not None:
            self.Display(depth+1,node.left)
        if node.right is not None:
            self.Display(depth+1,node.right)    

    
    def remove(self,data):
        if not self.root:
            print("The binary tree is empty")
            return
        if self.root.data == data:
            self.root = None

        self.recursiveremove(data,self.root)

    def recursiveremove(self,data,node):
        if node.left and node.left.data == data:
            node.left = None

        if node.right and node.right.data == data:
            node.right = None

        if node.left:
            self.recursiveremove(data,node.left)
        if node.right:
            self.recursiveremove(data,node.right)
    
    def search(self,data):
        nodefound = self.recursivesearch(data,self.root)

        if nodefound:
            print("true")

        else:
            print("false")    

    def recursivesearch(self,data,node):

        if not node or node.data == data:
            return node


        return self.recursivesearch(data,node.left) or self.recursivesearch(data,node.right)    




t2 = Binary_tree()
t2.Add(1)
t2.Add(2)
t2.Add(3)
t2.Add(4)
t2.Add(5)
t2.Add(6)
t2.Display()
t2.remove(4)
t2.Display()
t2.search(3)





        