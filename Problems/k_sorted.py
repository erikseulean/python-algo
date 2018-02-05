'''
get the regions of a k sorted array. 
k sorted array: 11,12,13,14,15,16,15,14,13,12,30,31,32,33,34,5,4,3,2,1
'''
from collections import namedtuple

array = [11, 12, 13, 14, 15, 16, 15, 14, 13, 12, 30, 31, 32, 33, 34, 5, 4, 3, 2, 1]

SubArray = namedtuple('SubArray', 'increasing, start, end')
SubArrayIndex = namedtuple('SubArrayIndex', 'array_index, index, value, increment')

def split_array(array):

    sub_arrays = []
    increasing = array[0] < array[1]
    
    start = 0
    for i in range(len(array) - 1):
        if (array[i] < array[i+1] and not increasing) or (array[i] > array[i+1] and increasing):
            sub_arrays.append(SubArray(increasing, start, i+1))
            increasing = not increasing
            start = i + 1

    sub_arrays.append(SubArray(increasing, start, len(array)))
    return sub_arrays

def sort_subarrays(array):
    sub_arrays = split_array(array)
    h = Heap()
    for array_index in enumerate(sub_arrays):
        if sub_array[index].increasing:
            h.enqueue(SubArrayIndex(index, sub_array[index].start, array[sub_array[index].start], 1))
        else: 
            h.enqueue(SubArrayIndex(index, sub_array[index].end, array[sub_array[index].end], -1))
    
    sorted_array = []
    while not h.Empty():
        item = h.dequeue()
        sorted_array.append(next.value)
        sub_array = sub_arrays[item.array_index]
        next_index = item.index + increment
        if next_index >= sub_array.start and next_index <= sub_array.end:
            h.enqueue(SubArrayIndex(item.index, next_index, array[next_index]), item.increment)
    
    return sorted_array    
