''' Longest increasing subsequence '''

def search(seq, number, numbers):
    left = 0
    right = len(seq) - 1

    while left < right:
        mid = left + (right - left) // 2
        if number > numbers[seq[mid]]:
            left = mid + 1
        elif number < numbers[seq[mid]]:
            right = mid
    return right


def lis(numbers) :
    if len(numbers) == 0:
        return
    sub = []
    sub.append(0)
    prev = [None for _ in range(len(numbers))]
    for i in range(len(numbers)):
        if len(sub) == 0 or numbers[i] > numbers[sub[-1]]:
            if len(sub) > 0:
                prev[i] = sub[-1]
            sub.append(i)
        else:
            pos = search(sub, numbers[i], numbers)
            sub[pos] = i
            if pos != 0:
                prev[pos] = sub[pos-1]

    parent = sub[-1]
    while parent is not None:
        print(numbers[parent])
        parent = prev[parent]

elem = [2, 6, 3, 4, 1, 2, 9, 5, 8]

lis(elem)

