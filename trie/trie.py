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
