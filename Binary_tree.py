


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


t2 = Binary_tree()
t2.Add(1)
t2.Add(2)
t2.Add(3)
t2.Add(4)


        