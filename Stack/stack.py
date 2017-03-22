from array import array


class ArrayStack(object):
    _array = array('H')
    size = 0
    elem = 0

    def __init__(self, size):
        self.size = size

    def insert(self, value):
        if len(self._array) == self.size:
            return
        self._array.append(value)
        self.elem += 1

    def pop(self):
        if len(self._array) is 0:
            return

        self.elem -= 1
        self._array.pop(self.elem)

    def print(self):
        print(self._array)
        print("")
