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

        elif not node.right:
            node.right = heapnode(data)    
            
        else:
            if     
