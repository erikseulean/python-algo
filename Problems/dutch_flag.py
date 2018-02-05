'''
arange the numbers in an array such as the smaller ones are before, followed by equal ones and ending with the bigger ones
'''

def partition(array, k):
    smaller = 0
    greater = len(array) - 1
    i = 0
    while i < greater:
        if array[i] < k:
            aux = array[smaller]
            array[smaller] = array[i]
            array[i] = aux
            smaller = smaller + 1
            i = i + 1
        elif array[i] > k:
            aux = array[greater]
            array[greater] = array[i]
            array[i] = aux
            greater = greater - 1
        else:
            i = i + 1
    

    return array


print(partition([5,4,7,1,3,3,2,5,7,3], 7))
print(partition([1,3,2,3,2,1,1,3,2,2,1,3], 2))