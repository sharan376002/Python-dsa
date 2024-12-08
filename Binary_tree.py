from typing import Self


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

        self.recursiveadd(data,self.root)

    def recursiveadd(data,node):
        if node.left is None:
            node.left = Node(data)

        elif node.right is None:
            node.right = Node(data)

        else:
             self.recursiveadd(data,node.left)  # we can pass also right side also        

        