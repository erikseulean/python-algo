'''
given an array find the kth smallest element
'''
from random import randint

def kth(array, start, end, k):
    piv = randint(start, end)
    pivot = array[piv]

    array[piv] = array[end]
    array[end] = pivot

    location = start
    for i in range(start, end):
        if array[i] < pivot:
            aux = array[location]
            array[location] = array[i]
            array[i] = aux
            location += 1

    array[end] = array[location]
    array[location] = pivot 
        
    if(location == k):
        return array[location]
    return kth(array, start, location, k) if (location > k) else kth(array, location, end, k)


a = [1, 4, 7, 2, 6, 1, 3, 9, 11, 12, 4, 9, 8, 10, 6]

assert kth(a, 0, len(a)-1, 4) == sorted(a)[4]
assert kth(a, 0, len(a) - 1, 8) == sorted(a)[8]
assert kth(a, 0, len(a)-1, 12) == sorted(a)[12]

