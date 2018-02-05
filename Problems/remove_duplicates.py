'''
remove duplicates from an array
'''

'''
array with sorted elements having duplicates.
when the duplicates are counting m, reduce the number of the duplicates to min(2,m)
'''


def remove_duplicates(array):

    location = 1
    for i in range(len(array) - 1):
        if array[i] != array[i+1]:
            array[location] = array[i+1]
            location = location + 1
    
    return array[0: location]

def remove_m_duplicates(array, m):
    location = 0
    start = 0
    for i in range(len(array)):
        if array[i] != array[start]:
            if i - start == m:
                location = location - (m - min(2, m))
            start = i
        array[location] = array[i]
        location = location + 1
    
    if len(array) - start == m:
        location = location - (m - min(2, m))

    return array[0:location]

print(remove_m_duplicates([1,1,1,1,2,2,2,2,3,3,3,4,4,5,5,5,5], 4))