# reterival - > get fetch the data 

# this data structure used in the backend 
# to used for word suggestion


# trie

class trieNode:
    def __init__(self):
        self.children = {}
        self.Isend = False


class Trie:
    def __init__(self):
        self.root = trieNode()

    def add(self,word):
        currentNode =self.root

        for char in word:

            if char not in currentNode.children:
                currentNode.children[char] = trieNode()

            currentNode  = currentNode.children[char]   

        currentNode.Isend  = True

    def search(self,word):

        currentNode =self.root

        for char in word:

            if char not in currentNode.children:
                return False
            
            currentNode  = currentNode.children[char]   

        if currentNode.Isend == True:
            return True
        
        return False


    def remove(self, word):
        if not self.search(word):
            print("word not found.. can't remove")
            return
        

        currentNode = self.root

        stack = []

        for char in word:
            stack.append(currentNode)
            currentNode = currentNode.children[char]

        currentNode.Isend = False
        while len(stack)>0
              