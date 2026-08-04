class Node:

    def __init__(self,data):

        self.data = data
        self.next = None

class LL:

    def __init__(self):

        self.head = None

    def reverse(self, data):

        prev = None

        cur = self.head


        while cur is not None:

            next_node = cur.next

            cur.next = prev

            prev = cur

            cur = next_node
