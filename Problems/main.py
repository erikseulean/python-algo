from Problems.linked_list_duplicates import remove_duplicates
from Problems.sort_list_by_x import  sort_by_x
from LinkedLists.linked_list import Node
from Problems.sum_linked_list import sum_lists


def create_list(l):
    head = Node(l[0])
    x = head
    for i in range (1, len(l)):
        n = Node(l[i])
        x.next = n
        x = x.next
    return head

first = create_list([7, 2, 6, 3, 1])
second = create_list([4, 9, 1, 8, 9])

res = sum_lists(first, second)

it = res
while it is not None:
    print(it.value)
    it = it.next
