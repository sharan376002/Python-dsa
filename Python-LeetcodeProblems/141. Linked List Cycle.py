

class Node:

    def __init__(self,data):

        self.data = data
        self.next = None

class LL:

    def __init__(self):

        self.head = None


    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        has  =  set()

        while head:

            if head not in has:
                has.add(head)
                head = head.next

            else:
                return True
            
        return False
        