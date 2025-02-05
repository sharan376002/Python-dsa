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


    def getparent(self,node,root)                
