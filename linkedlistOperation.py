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
    
    def printData(self):
        cur  =  self.head
        while(cur.pointer is not None):
            print(cur.data)
            cur = cur.pointer
    
    def remove(self,data):
        if (self.head is not None):
            if(self.head.data == data):
                self.head = self.head.pointer
                print("Succesfully the value removed from the node")
            else:
                cur = self.head

                while(cur.pointer is not None and cur.pointer.data != data):
                    cur = cur.pointer

                if cur.pointer is not None:
                    cur.pointer = cur.pointer.pointer
                    print("Succesfully the value removed from the Middle node")


                else:
                    print("the Remove value is not present in the linkid list")        



        
        else:
            print("the linkedlist is empty")    








l1 = linkedlistOpertation()
l1.add(1)
l1.add(2)
l1.add(5)
l1.add(6)

print(l1.remove(6))
print(l1.printData())

