class Node:

    def __init__(self,data):

        self.val = data
        self.next = None

class LL:

    def __init__(self):

        self.head = None


    def mergeKlist(self, lists):

        if not lists or len(lists) == 0:
            return None


        while len(lists) > 1:

            merged_list = []

            for i in range( 0 ,len(lists), 2):

                l1 = lists[i]
                l2 = lists[i+1] if lists[i+1] < len(lists) else None

                merged_list.append(self.merge(l1,l2))

            lists = merged_list

        return lists[0]


    def merge(self, l1,l2):

        dummy  = Node(0)

        cur = dummy


        while l1 and l2:

            if l1.val < l2.val:

                cur.next = l1
                l1 = l1.next

            else:

                cur.next  = l2
                l2 = l2.next

            cur = cur.next

        if l1:
            cur.next = l1

        elif l2:
            cur.next = l2


        return dummy.next