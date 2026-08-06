class Node:

    def __init__(self,data):

        self.data = data
        self.next = None

class LL:

    def __init__(self):

        self.head = None


    def reorderList(self,head):


        slow , fast =  head , head.next


        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next


        second = slow.next

        prev = None
        slow.next  = None

        while second:

            temp = second.next
            second.next = prev
            prev = second
            second = temp


        # merge the half

        first , second = head , prev


        while second:
            temp1 , temp2 = first.next , second.next
            first.next = second
            second.next = temp1
            first , second = temp1,temp2