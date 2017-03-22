from LinkedLists.linked_list import (
    Node
)


class ListStack(object):
    head = None
    elems = 0
    size = 0

    def __init__(self, size):
        self.size = size
        pass

    def push(self, value):
        if self.elems == self.size:
            return
        n = Node(value)
        n.next = None
        if self.head is None:
            self.head = n
            return
        n.next = self.head
        self.head = n
        self.elems += 1
        print(self.head)

    def pop(self):
        if self.head is None:
            return
        self.head = self.head.next

    def print(self):
        it = self.head
        while it:
            print(it.value)
            it = it.next
        print("")
