''' kth prime with 3,5,7 as prime factors '''
from queue import Queue

def init():
    three = Queue()
    five = Queue()
    seven = Queue()
    three.put(1)
    return three, five, seven


def kth(k):
    three, five, seven = init()

    for _ in range(0, k+1):
        t = three.queue[0]
        f = five.queue[0] if len(five.queue) != 0 else 10000
        s = seven.queue[0] if len(seven.queue) != 0 else 10000
        val = min(t, min(f, s))
        if val == t:
            three.get()
            three.put(3 * val)
            five.put(5 * val)
        elif val == f:
            five.get()
            five.put(5 * val)
        else:
            seven.get()
            seven.put(7*val)
    return val


print(kth(4))
# print(kth(6))
# print(kth(7))
# print(kth(8))
# print(kth(9))
# print(kth(10))