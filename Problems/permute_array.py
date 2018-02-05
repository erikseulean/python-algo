'''
given an array and a permutation, apply the permutation on the array
'''


def apply_permutation(array, p):

    i = 0
    while i != len(array):
        if i != p[i]:
            aux = array[p[i]]
            array[p[i]] = array[i]
            array[i] = aux

            aux = p[p[i]]
            p[p[i]] = p[i]
            p[i] = aux
        else:
            i = i + 1
        
    return array

print(apply_permutation(['a','b','c', 'd'], [3,2,1,0]))