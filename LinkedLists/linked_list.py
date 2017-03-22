
class Node(object):
    next = None
    value = None

    def __init__(self, value):
        self.value = value
        pass


class LinkedList(object):

    head = None

    def __init__(self):
        pass

    def insert_first(self, node):
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def print(self):
        it = self.head
        while it is not None:
            print(str(it.value))
            it = it.next

    def remove(self, value):
        if self.head.value == value:
            self.head = self.head.next
            return
        prev = self.head
        next = self.head.next
        while next is not None:
            if next.value == value:
                prev.next = next.next
                return
            prev = next
            next = next.next

    def insert_after(self,value, ins_value):
        prev = self.head
        next = self.head.next
        while prev is not None:
            if prev.value == value:
                n = Node(ins_value)
                n.next = next
                prev.next = n
                return
            prev = prev.next
            next = next.next if next is not None else None
