class node:
    def __init__(self,data):
        self.data = data
        self.pointer  = None


class linkedlistOpertation:
    def __init__(self):
        self.head = None

    def add(self,data):
        NewNode = node(data)
        if self.head is None:
            self.head = NewNode
        else:
            cur = self.head

            while(cur.pointer is not None):
                cur = cur.pointer
            cur.pointer = NewNode                    
