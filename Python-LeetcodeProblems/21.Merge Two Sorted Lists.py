class Node:

    def __init__(self,data):

        self.data = data
        self.next = None

class LL:

    def __init__(self):

        self.head = None

    def mergerTOLL(self,l1,l2):

        dummy = Node(0)

        curr = dummy


        while l1 and l2:

            if l1.data < l2.data:
                curr.next = l1
                l1 = l1.next

            else:
                curr.next  = l2
                l2 = l2.next

            curr = curr.next


        if l1:
            curr.next  = l1

        elif l2:
            curr.next = l2

        return dummy.next




def display(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")





l1 = Node(1)
l1.next = Node(3)
l1.next.next = Node(5)
l1.next.next.next = Node(7)

# Create List 2: 2 -> 4 -> 6 -> 8
l2 = Node(2)
l2.next = Node(4)
l2.next.next = Node(6)
l2.next.next.next = Node(8)


ll = LL()
merged = ll.mergerTOLL(l1, l2)



print("Merged List:")
display(merged)