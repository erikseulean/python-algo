

class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

head = Node(12, Node(7, Node(3), Node(9, Node(8), Node(11))), Node(15, Node(13), Node(17)))

def LCA(head, first, second):

    lca_node = None

    def find(node, first, second):
        nonlocal lca_node
        if not node or lca_node: 
            return 0

        left = find(node.left, first, second)
        right = find(node.right, first, second)

        total = left + right + (node.value == first) + (node.value == second)

        if total == 2 and not lca_node:
            lca_node = node
        
        return total

    find(head, first, second)
    print(lca_node.value)


LCA(head, 13, 15)