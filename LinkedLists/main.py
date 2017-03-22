from linked_list import (
    Node,
    LinkedList
)


def main():
    list = LinkedList()
    list.insert_first(Node(5))
    list.insert_first(Node(4))
    list.insert_first(Node(3))
    list.insert_first(Node(2))
    list.insert_first(Node(1))

    list.print()
    print("")
    list.remove(3)
    list.insert_after(2,10)
    list.print()
    list.remove(5)
    list.insert_after(4,20)
    print("")
    list.insert_after(100,5)
    list.print()


if __name__ == '__main__':
    main()
