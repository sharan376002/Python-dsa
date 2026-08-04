

class Node:

    def __init__(self,data):

        self.data = data
        self.next = None

class LL:

    def __init__(self):

        self.head = None

    def insertAtEnd(self,data):

        newnode = Node(data)

        if self.head == None:
            self.head = newnode
            return

        temp  = self.head

        while temp.next:
            temp  = temp.next

        temp.next  = newnode

    def display(self):
            temp = self.head
            while temp:
                print(temp.data, end=" -> ")
                temp = temp.next
            print("None")


l1 = LL()

l1.insertAtEnd(10)
l1.insertAtEnd(20)
l1.insertAtEnd(30)

l1.display()


        


