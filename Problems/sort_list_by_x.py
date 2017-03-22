'''
Arrange elements in a linked list such as all smaller then x should be at the beginning and the greater nodes at the end
'''

def sort_by_x(x, linked_list):
    if linked_list is None or linked_list.next is None:
        return

    first = linked_list
    while first is not None and first.value < x:
        first = first.next

    if first is None:
        return

    head = linked_list
    it = first
    while it.next is not None:
        if it.next.value < x:
            node = it.next
            it.next = node.next
            node.next = head
            head = node
        else:
            it = it.next
    return head