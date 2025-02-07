# minheap

class heapnode:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


class minheap:
    
    def __init__(self):
        
        self.root = None

    def add(self,data):

        if not self.root:
            self.root = heapnode(data)
            return
        
        self.recursiveadd(data,self.root)


    def recursiveadd(self,data,node):
        if not node.left:
            node.left = heapnode(data)
            self.heapifyup(node.left)

        elif not node.right:
            node.right = heapnode(data)
            self.heapifyup(node.right)

            
        else:
            if  self.getcount(node.left) <= self.getcount(node.right):
                self.recursiveadd(data,node.left)

            else:
                self.recursiveadd(data,node.right)       


    def getcount(self,node):
        if not node:
            return 0

        return 1 + self.getcount(node.left) + self.getcount(node.right)     



    def heapifyup(self,node):
        while node and node != self.root:
            parentnode  = self.getparent(node,self.root)
            if parentnode.data > node.data:
                parentnode.data , node.data = node.data,parentnode.data
                node = parentnode

            else:
                break



    def getparent(self,node,root):
        if node.left == node or root.right == node:
            return root

        if root.left:
            parent = self.getparent(node,root.left)
            if parent: return parent
        
        if root.right:
             parent = self.getparent(node,root.right)
             if parent: return parent



heapnode = minheap()
