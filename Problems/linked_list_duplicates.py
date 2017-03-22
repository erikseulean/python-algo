'''
Remove duplicates from a linked list
'''


def remove_duplicates(linked_list):
    first = linked_list
    second = linked_list
    while first.next is not None:
        while second.next is not None:
            if second.next.value == first.value:
                second.next = second.next.next
            else:
                second = second.next
        first = first.next
        second = first