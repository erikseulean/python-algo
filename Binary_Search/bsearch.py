

def search(nr, array):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nr == array[mid]:
            return mid
        elif nr > array[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return -1


print(search(3, [1,2,3,4,5,6,7]))
print(search(6, [1,2,3,4,5,6,7]))
print(search(7, [1,2,3,4,5,6,7]))
print(search(1, [1,2,3,4,5,6,7,8]))
print(search(9, [1,2,3,4,5,6,7]))
