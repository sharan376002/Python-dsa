class Node:

    def __init__(self,data):

        self.data = data
        self.next = None

class LL:

    def __init__(self):

        self.head = None



    def remove(self, head, n):

        if head <= 1:
            return None


        
        dummy = Node(0,head)

        slow = dummy

        fast = head

        for i in range(n):
            fast = fast.next

        while fast is not None:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next



        return dummy.next

