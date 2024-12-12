
# before seeing the coding see the txt file
class BSTnode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None


    def display(self):

        result = []
        print("Select the which order u wan to do in the tree")
        print("\n 1. Inorder \n 2. preOrder  \n 3.Post Order")
        choice = int(input("Enter the choice btw them : "))
        if choice==1:
            print("Inorder: ")
            self.recursiveInorder(self.root,result)
            print(result)

        elif choice==2:
            print("Preorder : ")
            self.preordertravsal(self.root,result)
            print(result)


        elif choice==3:
            self.postordertravsal(self.root,result)
            print(result)

            



        print(result)

    def recursiveInorder(self,node,result):
        if not node:
            return None
        
        else:
            self.recursiveInorder(node.left,result)
            result.append(node.data)
            self.recursiveInorder(node.right,result)



    def preordertravsal(self,node,result):
        if not node:
            return None
        
        else:
            result.append(node.data)
            self.recursiveInorder(node.left,result)
            self.recursiveInorder(node.right,result)


    def postordertravsal(self,node,result):
        if not node:
            return None
        
        else:
            self.recursiveInorder(node.left,result)
            self.recursiveInorder(node.right,result)
            result.append(node.data)


