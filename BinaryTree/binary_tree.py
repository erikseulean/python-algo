
class BinaryTree(object):
    left = None
    right = None
    value = None

    def __init__(self, value):
        self.value = value

    def add_left(self, left):
        self.left = left

    def add_right(self, right):
        self.right = right


def iterate(binary_tree):
        if binary_tree is None:
            return
        print(str(binary_tree.value))
        iterate(binary_tree.left)
        iterate(binary_tree.right)
