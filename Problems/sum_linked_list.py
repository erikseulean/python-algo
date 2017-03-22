'''
Given two linked lists, representing digits, sum them up to get only one number
'''
from LinkedLists.linked_list import Node

def sum_lists(first, second):
    if first is None:
        return second
    if second is None:
        return first

    head = Node(0)
    carry = 0
    it = head
    while first and second:
        next = (first.value + second.value + carry) % 10
        carry = (first.value + second.value + carry) // 10
        it.next = Node(next)
        it = it.next
        first = first.next
        second = second.next

    node = None
    if first is None:
        node = second
    else:
        node = first

    while node:
        next = (node.value + carry) % 10
        carry = (node.value + carry) // 10
        it.next = Node(next)
        it = it.next
        node = node.next
    if carry == 1:
        it.next = Node(1)

    return head.next