from LinkedLists.linked_list import (
    Node
)

class Queue(object):
    head = None
    tail = None

    def __init__(self):
        pass

    def push(self, value):
        n = Node(value)
        if self.head is None:
            self.head = n
            self.tail = n
        else:
            self.tail.next = n
            self.tail = self.tail.next

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
