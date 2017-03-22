

def sort(left, right, array):
    if left >= right:
        return
    mid = left + (right - left) // 2
    sort(left, mid, array)
    sort(mid+1, right, array)
    merge(left, right, array)


def merge(left, right, array):
    mid = left + (right - left) // 2
    len1 = mid - left + 1
    len2 = right - mid
    first = [0 for i in range(len1)]
    second = [0 for i in range(len2)]

    for i in range(len1):
        first[i] = array[left + i]
    for i in range(len2):
        second[i] = array[i + mid + 1]

    i = 0
    j = 0
    for k in range(left, right+1):
        if j == len2 or (i != len(first) and first[i] < second[j]):
            array[k] = first[i]
            i += 1
        else:
            array[k] = second[j]
            j += 1


array = [4,7,8,1,4,9,4,5,12,3,5,7]
sort(0, len(array)-1, array)
print(array)
