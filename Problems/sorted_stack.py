

class SortedStack(object):
    help_stack = []
    stack = []

    def push(self, value):
        if len(self.stack) == 0:
            self.stack.append(value)
        else:
            while len(self.stack) is not 0 and self.stack[len(self.stack) - 1] > value:
                self.help_stack.append(self.stack.pop())
            self.stack.append(value)
            while len(self.help_stack) is not 0:
                self.stack.append(self.help_stack.pop())

    def print_stack(self):
        print(self.stack)


sorted_stack = SortedStack()
sorted_stack.push(5)
sorted_stack.push(2)
sorted_stack.push(3)
sorted_stack.push(7)
sorted_stack.push(4)
sorted_stack.push(1)
sorted_stack.push(9)
sorted_stack.push(6)
sorted_stack.push(2)
sorted_stack.push(8)
sorted_stack.push(4)
sorted_stack.push(5)

sorted_stack.print_stack()
