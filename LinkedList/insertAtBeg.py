
class Node:

    def __init__(self,data):

        self.data = data
        self.next = None

class LL:

    def __init__(self):

        self.head = None

    def insert_at_beg(self,data):

        newnode = Node(data)

        newnode.next = self.head

        self.head = newnode

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")





l1 = LL()

l1.insert_at_beg(10)
l1.insert_at_beg(20)
l1.insert_at_beg(30)

l1.display()